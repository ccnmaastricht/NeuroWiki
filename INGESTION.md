# INGESTION.md

```
Read AGENT.md fully, then read INGESTION.md fully.
Process the following PDF(s), one at a time, following this workflow exactly:
- raw/<filename>.pdf
Print the session summary when done.
```

> **Note:** `raw/` is git-ignored, so the `@` file picker in most agents will not list its contents. Type the path directly (e.g. `raw/smith2023.pdf`) rather than using the picker.

---

## Rules

- Process one PDF at a time. Complete all steps before starting the next.
- The structured abstract constructed in Step 2 is a processing tool only. Do not output it to the conversation; it is not stored.
- Never modify files in `raw/`.

---

## Step 1 — Check for Prior Secondary Entry

Search `secondary.bib` for an entry matching this paper by author, year, and title.

- **Found**: this is a promotion. Note the existing key — it will be reused.
- **Not found**: proceed.

---

## Step 2 — Read and Extract

Read the full PDF. Internally construct a structured abstract:
- **Background**: what gap or question motivated this work?
- **Methods**: experimental design, model, or analysis used
- **Key findings**: specific results, including magnitudes where reported
- **Limitations**: author-acknowledged and agent-identified

Use this to determine which existing pages are affected, whether new pages are needed, and which claims belong on which pages.

---

## Step 3 — Update primary.bib

Add a complete BibTeX entry to `wiki/primary.bib`, all fields verified against the PDF:

```bibtex
@article{AuthorYYYY,
  author  = {},
  title   = {},
  journal = {},
  year    = {},
  volume  = {},
  pages   = {},
  doi     = {},
  annote  = {<one-line description of main contribution>}
}
```

**If promotion**: move the entry from `secondary.bib` to `primary.bib`. Complete uncertain fields. Remove `note = {reconstructed...}`. Retain the same key.

---

## Step 4 — Update secondary.bib

For each paper cited within the PDF that is relevant to this project (per Section 1 of AGENT.md) and not already in `raw/`, add an entry to `secondary.bib` if not already present:

```
note = {reconstructed from @CitationKey}
annote = {<contribution, if inferable>}
```

---

## Step 5 — Update or Create Wiki Pages

For each affected concept page, rewrite or create it using the templates in AGENT.md Section 6.

- Freely rewrite any section when new evidence warrants it
- Synthesize across sources; cite each claim with `(@Key)` or `(@Key†)`
- Apply conflict resolution per AGENT.md Section 8 when this paper contradicts existing claims
- Apply citation integrity rules per AGENT.md Section 9 when reading existing content
- Never delete a claim without replacing it or moving it to Controversies with an explanatory note
- Update confidence when new evidence warrants it; document the change in Controversies

**If promotion**, after updating `primary.bib`:
1. Global find-and-replace across all pages: `(@Key†)` → `(@Key)` for this key
2. Re-evaluate every claim that previously cited this paper as secondary — rewrite any the primary source contradicts or nuances
3. Scan all pages and both `.bib` files to confirm no `(@Key†)` instances or `secondary.bib` entries remain for this key; report any unresolved instances
4. Note which claims were revised during promotion on the affected pages

---

## Step 6 — Update wiki/index.md

Add or update every new or modified page in `wiki/index.md` under the correct section.
Use relative markdown paths: `[TYPE_slug](pages/TYPE_slug.md)`.
Update the `updated` field in the frontmatter.

---

## Step 7 — Session Summary

```
## Ingestion Session — <filename> — YYYY-MM-DD

PDF processed: <filename>
Promotion: yes (@Key) / no

Pages created: 
Pages modified: 
Secondary entries added: 
Promotion cleanup: confirmed clean / unresolved: 

Confidence changes:
- <page>: <old> → <new> — <justification>

Conflicts requiring human review (⚑):
- <page>: <issue>

Citation integrity flags added:
- <page>: <claim>

Unresolved citations:
- <description>
```
