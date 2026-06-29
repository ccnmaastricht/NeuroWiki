# REFINE_B.md — Depth Audit

```
Read AGENT.md fully, then read REFINE_B.md fully.
Run the Depth Audit across all pages in wiki/pages/.
Follow this workflow exactly. Save the report and print the session summary when done.
```

---

## Rules

This workflow does not modify any wiki pages.
It produces a report saved to `wiki/depth-audit-YYYY-MM-DD.md` and stops there.
Gaps identified here are filled by ingesting more PDFs — not by writing from agent knowledge.

---

## Step B1 — Derive Project-Specific Questions

Read Section 1 of AGENT.md. From the research question, model types, brain regions, and key phenomena listed there, derive 3–5 concrete questions per category below that are specific to this project. Generate these fresh — do not reuse examples from this file. Record the derived questions at the top of the audit report (Step B3) so future readers know what standard was applied.

### The four depth categories

**Category 1 — Quantitative parameters**
Can a reader extract specific numerical values sufficient to constrain the project's model or interpret its data? A page fails if quantitative claims are vague, absent, or presented as ranges too wide to be useful.

**Category 2 — Connectivity and structural specifics**
Can a reader determine structural relationships at the resolution needed to implement or justify a model? A page fails if connectivity is described only at region-to-region level where finer resolution matters for the project.

**Category 3 — Species and preparation generality**
Can a reader determine the boundary conditions of reported findings — species, brain state, recording method, developmental stage, in vivo vs in vitro? A page fails if findings are presented without indication of the conditions under which they were obtained.

**Category 4 — Functional role and project relevance**
Can a reader connect this entity to the specific computations or behaviors the project models? A page fails if the functional role is described only in general terms without engagement with the project's research question.

Not all categories apply equally to all page types. Use judgment: PAR_ pages are rarely judged on Category 2; MOD_ pages are rarely judged on Category 3. Weight Category 4 for all types.

---

## Step B2 — Audit Each Page

For each page in `wiki/pages/`, attempt to answer the project-specific questions derived in Step B1. Rate each applicable category:

- ✅ **Passes** — questions answerable from page content with citations
- ⚠️ **Partial** — questions partially answerable; note what is missing
- ❌ **Fails** — questions not answerable from this page

---

## Step B3 — Save the Audit Report

Save to `wiki/depth-audit-YYYY-MM-DD.md`:

```markdown
---
type: audit
title: Depth Audit YYYY-MM-DD
updated: YYYY-MM-DD
---

# Depth Audit — YYYY-MM-DD

## Project-specific questions used

<Paste derived questions from Step B1 here, grouped by category.>

## Summary

| Tier | Count |
|------|-------|
| No gaps | N |
| Minor gaps (1 category partial or failing) | N |
| Major gaps (2+ categories partial or failing) | N |
| Total pages audited | N |

## Major gaps

### [PHE_example](pages/PHE_example.md)
- ❌ Category 1: <what is missing>
- ❌ Category 3: <what is missing>
- ⚠️ Category 2: <what is partial>
- Recommended action: <what types of PDFs would fill these gaps>

## Minor gaps

### [TYPE_slug](pages/TYPE_slug.md)
- ⚠️ Category 4: <what is partial>
- Recommended action: <brief note>

## No gaps

<List of pages that passed all applicable categories.>

## PDF acquisition priorities

<Ordered list of topic areas where the wiki is thinnest.
This directly guides which PDFs to add in the next ingestion sessions.>

1. <topic / question area> — needed for: <pages>
2. 
```

---

## Step B4 — Write Session Log Entry

Append a new entry to `wiki/log.md` (after the opening `---`, newest first) using the canonical format from AGENT.md Section 11. Print the entry to the conversation.

For the **Changes** section, include:

```
- Pages audited: N
- No gaps: N | Minor gaps: N | Major gaps: N
- Audit report: wiki/depth-audit-YYYY-MM-DD.md
- Top PDF acquisition priorities: <1. topic — for pages; 2. topic — for pages; 3. topic — for pages>
```

Note: REFINE_B writes no wiki pages. Leave **Flags raised** and **Flags resolved** as "none" unless citation issues were discovered while reading.
