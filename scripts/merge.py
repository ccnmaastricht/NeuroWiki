#!/usr/bin/env python3
"""
NeuroWiki merge.py
Handles mechanical deduplication, conflict detection, and bib merging
before the agent synthesizes matching pages.

Usage:
    python3 merge.py --source <path-to-submitted-wiki> --target <community-wiki-path> --report <output.json>
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from datetime import date


# ── YAML frontmatter parsing (no external deps) ──────────────────────────────

def parse_frontmatter(text):
    """Extract YAML frontmatter dict and body from a markdown file."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, body


def validate_page(path, fm, body):
    """Return list of validation errors for a page."""
    errors = []
    required_all = ["type", "title", "updated"]
    confidence_types = {"phenomenon", "model", "region"}
    for field in required_all:
        if field not in fm or "MISSING" in str(fm.get(field, "")):
            errors.append(f"Missing required frontmatter field: {field}")
    if fm.get("type") in confidence_types:
        if "confidence" not in fm or "MISSING" in str(fm.get("confidence", "")):
            errors.append("Missing confidence field")
    if "SECTION STUB" in body and body.count("SECTION STUB") > 2:
        errors.append("Page is mostly stubs — insufficient content for community submission")
    return errors


# ── BibTeX helpers ────────────────────────────────────────────────────────────

def parse_bib(bib_path):
    """Parse a .bib file into a dict keyed by citation key."""
    entries = {}
    if not bib_path.exists():
        return entries
    text = bib_path.read_text(encoding="utf-8")
    for match in re.finditer(r"@\w+\{(\w+),(.*?)\n\}", text, re.DOTALL):
        key = match.group(1)
        entries[key] = match.group(0)
    return entries


def merge_bib(source_entries, target_entries):
    """Merge source into target. Return (merged, conflicts)."""
    merged = dict(target_entries)
    conflicts = []
    for key, entry in source_entries.items():
        if key not in target_entries:
            merged[key] = entry
        elif entry.strip() != target_entries[key].strip():
            conflicts.append({"key": key, "issue": "Same key, different metadata"})
    return merged, conflicts


# ── Page scanning ─────────────────────────────────────────────────────────────

def scan_wiki(wiki_path):
    """Return dict of slug -> (path, frontmatter, body) for all pages."""
    pages = {}
    pages_dir = Path(wiki_path) / "pages"
    if not pages_dir.exists():
        return pages
    for p in pages_dir.glob("*.md"):
        text = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        pages[p.stem] = {"path": p, "fm": fm, "body": body}
    return pages


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="NeuroWiki merge script")
    parser.add_argument("--source", required=True, help="Path to submitted project wiki root")
    parser.add_argument("--target", required=True, help="Path to community wiki root")
    parser.add_argument("--report", required=True, help="Output JSON report path")
    parser.add_argument("--lab", default="Unknown Lab", help="Contributing lab name")
    args = parser.parse_args()

    source_path = Path(args.source)
    target_path = Path(args.target)
    report = {
        "date": date.today().isoformat(),
        "submitted_by": args.lab,
        "new_pages": [],
        "matching_pages": [],
        "structural_errors": [],
        "bib_conflicts": [],
        "summary": {}
    }

    # Scan pages
    source_pages = scan_wiki(source_path)
    target_pages = scan_wiki(target_path)

    # Validate and classify
    for slug, data in source_pages.items():
        errors = validate_page(data["path"], data["fm"], data["body"])
        if errors:
            report["structural_errors"].append({"slug": slug, "errors": errors})
            continue
        if slug in target_pages:
            report["matching_pages"].append({
                "slug": slug,
                "source_confidence": data["fm"].get("confidence", "unknown"),
                "target_confidence": target_pages[slug]["fm"].get("confidence", "unknown"),
                "action": "requires_synthesis"
            })
        else:
            report["new_pages"].append({
                "slug": slug,
                "type": data["fm"].get("type", "unknown"),
                "source_confidence": data["fm"].get("confidence", "unknown"),
                "action": "add_to_community"
            })

    # Merge bib files
    source_bib = parse_bib(source_path / "primary.bib")
    source_bib.update(parse_bib(source_path / "secondary.bib"))
    target_bib = parse_bib(target_path / "references.bib")
    _, bib_conflicts = merge_bib(source_bib, target_bib)
    report["bib_conflicts"] = bib_conflicts

    # Summary
    report["summary"] = {
        "pages_in_submission": len(source_pages),
        "new_pages": len(report["new_pages"]),
        "matching_pages": len(report["matching_pages"]),
        "structural_errors": len(report["structural_errors"]),
        "bib_conflicts": len(bib_conflicts),
        "proceed": len(report["structural_errors"]) == 0
    }

    if not report["summary"]["proceed"]:
        print(f"[merge.py] Structural errors found. Do not proceed with agent synthesis.")
        print(f"[merge.py] Return the submission with the error list in {args.report}")
    else:
        print(f"[merge.py] Validation passed. Proceed to agent synthesis.")
        print(f"[merge.py]   New pages:      {report['summary']['new_pages']}")
        print(f"[merge.py]   Matching pages: {report['summary']['matching_pages']}")
        print(f"[merge.py]   Bib conflicts:  {report['summary']['bib_conflicts']}")

    Path(args.report).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"[merge.py] Report written to {args.report}")
    sys.exit(0 if report["summary"]["proceed"] else 1)


if __name__ == "__main__":
    main()
