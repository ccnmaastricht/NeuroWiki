# REFINE_C.md — Cross-Link Audit

```
Read AGENT.md fully, then read REFINE_C.md fully.
Run the Cross-Link Audit across all pages in wiki/pages/ and wiki/index.md.
Follow this workflow exactly. Print the session summary when done.
```

---

## Linking Rules

### Add a link when ALL of the following are true

1. The concept is mentioned by name or a recognized synonym in the page text
2. A wiki page exists for that concept
3. It is the first mention within the current `##` section
4. The mention is substantive — the concept is directly relevant to the claim being made

### Do NOT add a link when ANY of the following are true

- The concept has already been linked earlier in the same `##` section
- The target page contains only stub content
- The mention is incidental background phrasing
- The link would fall inside a heading, metadata field, or citation
- The concept already appears in the page's `related` frontmatter field

### Remove a link when

- The same concept is linked more than once within a single `##` section — keep the first, remove the rest

---

## Step C1 — Build the Link Index

Scan all pages in `wiki/pages/` and build an internal index:
- Each page slug → canonical concept name (from the page `title` frontmatter field)
- Synonyms and abbreviations → same slug, inferred from page titles and body content only

When uncertain whether a term refers to the same concept as a page, do not link.

---

## Step C2 — Audit Each Page

For every page in `wiki/pages/`:

1. Read each `##` section in sequence, resetting the linked-concepts tracker at each new section
2. For each unlinked mention: check all conditions in the linking rules above
3. For each existing link: check whether it is a duplicate within the same section

Also audit `wiki/index.md`: ensure every page in `wiki/pages/` has a corresponding entry with a correct relative path link. Add missing entries; flag broken paths.

---

## Step C3 — Apply Changes

Changes are surgical: wrap or unwrap the concept name in `[[TYPE_slug]]`. Do not alter surrounding text.

Synonym resolution: link the exact term as written — do not replace it with the canonical name.
Use aliased link syntax if supported: `[[REG_v1|striate cortex]]`.
Otherwise link the slug and leave the term as-is in the surrounding prose.

---

## Step C4 — Write Session Log Entry

Append a new entry to `wiki/log.md` (after the opening `---`, newest first) using the canonical format from AGENT.md Section 11. Print the entry to the conversation.

For the **Changes** section, include:

```
- Pages audited: N
- Pages modified: N
- Links added: N total (<page: +N, ...>)
- Redundant links removed: N total (<page: -N, ...>)
- Synonyms resolved: <"term" → [[TYPE_slug]] on page, or "none">
- index.md entries added: <list or "none">
- Broken paths fixed: <list or "none">
- Concepts with no existing page: <"concept" — mentioned on pages, or "none">
```

List any concepts with no existing page under **Action items** as candidates for future pages.
