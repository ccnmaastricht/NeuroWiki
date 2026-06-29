# REFINE_A.md — Structural Harmonization

```
Read AGENT.md fully, then read REFINE_A.md fully.
Run Structural Harmonization across all pages in wiki/pages/ and wiki/index.md.
Follow this workflow exactly. Print the session summary when done.
```

---

## Rules

This workflow does not add, remove, or rewrite content.
It only restructures, reformats, and repairs metadata.
If a required section is missing, add a stub — never invented text.

---

## Step A1 — Canonical Structure Checklist

### YAML frontmatter — required fields by type

| Type | Required frontmatter fields |
|------|-----------------------------|
| All pages | `type`, `title`, `updated` |
| PHE_, MOD_, REG_ | + `confidence` |
| THE_ | + `status` |
| MOD_ | + `subtype` |
| All pages | `related` (list; empty list `[]` acceptable if no links yet) |

Valid `type` values: `phenomenon`, `model`, `theory`, `region`, `paradigm`, `index`

### Section order by page type

| Type | Required sections, in order |
|------|-----------------------------|
| PHE_ | Description · Empirical Basis · Key Parameters and Quantitative Signatures · Generality · Controversies · Modeling Implications |
| MOD_ | Description · Formal Description · Core Assumptions · Empirical Support · Empirical Challenges · Comparison to Alternatives · Controversies · Usage in the Literature |
| THE_ | Core Claims · Explanatory Schema · Model Family · Mechanistic Grounding · Empirical Scope · Controversies · Key Sources |
| REG_ | Anatomical Identity · Physiology · Connectivity · Functional Role(s) · Controversies · Modeling Considerations |
| PAR_ | Description · What It Measures / Reveals · Standard Variants · Limitations and Confounds · Key Studies and Datasets · Relevance to This Project |

### Notation standards

- Citations: `(@Key)` or `(@Key†)` — not bare `Key`, `[Key]`, or `(Key)`
- Cross-links in page bodies: `[[TYPE_slug]]`
- Links in `wiki/index.md`: relative markdown paths `(pages/TYPE_slug.md)`
- LaTeX: `$...$` inline, `$$...$$` block
- No `PAP_` prefixes anywhere (deprecated)

---

## Step A2 — Audit Each Page

For every file in `wiki/pages/` and `wiki/index.md`:

1. Check YAML frontmatter is present and contains all required fields for the page type
2. Check all required sections are present and in canonical order
3. Check no non-canonical heading names are used
4. Check citation, link, and LaTeX notation conforms to standards above

---

## Step A3 — Repair Each Page

| Issue | Action |
|-------|--------|
| Missing frontmatter block | Add block with all fields set to `<!-- MISSING -->` |
| Missing required frontmatter field | Add field with `<!-- MISSING -->` value |
| Missing section | Add heading + `<!-- SECTION STUB: populate in next ingestion session -->` |
| Wrong section order | Reorder verbatim — do not alter content |
| Non-canonical heading | Rename — do not alter content |
| Inconsistent citation notation | Correct to `(@Key)` or `(@Key†)` |
| Inconsistent link notation | Correct to `[[TYPE_slug]]` in bodies; relative paths in `index.md` |
| Malformed LaTeX delimiters | Correct delimiters only — do not alter equation content |

---

## Step A4 — Write Session Log Entry

Append a new entry to `wiki/log.md` (after the opening `---`, newest first) using the canonical format from AGENT.md Section 11. Print the entry to the conversation.

For the **Changes** section, include:

```
- Pages audited: N
- Pages with no issues: N
- Pages repaired: N
- Missing frontmatter fields added: <page: field, or "none">
- Missing sections stubbed: <page: section, or "none">
- Section reordering: <page, or "none">
- Heading renames: <page: old → new, or "none">
- Notation corrections: N instances across M pages (or "none")
```

List any `<!-- MISSING -->` stubs added under **Action items** so the human knows what needs populating in the next ingestion session.
