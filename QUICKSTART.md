# QUICKSTART.md — Setup and Usage Guide

---

## Session Invocation Prompts

Copy the relevant prompt and paste it at the start of an agent session.

### Ingestion — single PDF
```
Read AGENT.md fully, then read INGESTION.md fully.
Process the following PDF, following the workflow in INGESTION.md exactly:
- raw/<filename>.pdf
Print the session summary when done.
```

### Ingestion — batch
```
Read AGENT.md fully, then read INGESTION.md fully.
Process the following PDFs one at a time, completing all steps before moving to the next:
- raw/paper1.pdf
- raw/paper2.pdf
- raw/paper3.pdf
Print a combined session summary when done.
```

```
Read AGENT.md fully, then read INGESTION.md fully.
Process all PDFs in raw/ one at a time, completing all steps before moving to the next.
Print a combined session summary when done.
```

> **Note on file picking:** Because `raw/` is git-ignored, the `@` file picker in Claude Code and similar agents will not list files inside it. Just type the path directly (e.g. `raw/smith2023.pdf`).

### Refinement A — Structural harmonization
```
Read AGENT.md fully, then read REFINE_A.md fully.
Run Structural Harmonization across all pages in wiki/pages/ and wiki/index.md.
Follow REFINE_A.md exactly. Print the session summary when done.
```

### Refinement B — Depth audit
```
Read AGENT.md fully, then read REFINE_B.md fully.
Run the Depth Audit across all pages in wiki/pages/.
Follow REFINE_B.md exactly. Save the report and print the session summary when done.
```

### Refinement C — Cross-link audit
```
Read AGENT.md fully, then read REFINE_C.md fully.
Run the Cross-Link Audit across all pages in wiki/pages/ and wiki/index.md.
Follow REFINE_C.md exactly. Print the session summary when done.
```

### Writing assistance — background / introduction
```
I am writing the introduction to a paper on [TOPIC].
Using the wiki pages, draft a background section covering: [subtopics].
Use (@Key) citation notation. Flag any debated or speculative claims.
Do not process any new PDFs.
```

### Writing assistance — assessing a methodological choice
```
I need to evaluate our choice of [MODEL/METHOD].
Critically evaluate the empirical support, core assumptions and biological basis,
and how it compares to [ALTERNATIVE].
Draw from MOD_, PHE_, THE_, and REG_ pages. Do not process any new PDFs.
```

### Wiki overview
```
Give me an overview of the current wiki: which phenomena are well-covered vs thin,
which pages are speculative, and what topics seem underrepresented given
the research question in Section 1. Do not process any new PDFs.
```

---

## Setting Up a New Project

Create one copy of this template per project or research line.

1. On GitHub, click **Use this template → Create a new repository** on the [NeuroWiki template repo](https://github.com/ccnmaastricht/NeuroWiki), then clone your new repo
2. Open `AGENT.md` and complete every field marked with a blank in Section 1.
3. Run the setup script:
   ```bash
   bash setup.sh "My Project Name"
   ```
4. Add PDFs to `raw/` and run your first ingestion session

---

## Refinement Schedule

| Trigger | Run |
|---------|-----|
| After every 5–10 PDFs ingested | REFINE_A + REFINE_C |
| Monthly | REFINE_B |
| Before an empirical/modeling phase or manuscript | REFINE_A then REFINE_B |
| When a new contributor joins | REFINE_A |
| After REFINE_C identifies candidate pages | Next ingestion session |

---

## After Every Session

1. Read the agent's session summary
2. Complete the VERIFICATION.md post-session checklist
3. Add a signed entry to `wiki/log.md`

No wiki content should be used for methodological decisions or manuscript writing until the session checklist is signed off.

---

## Tips for Users

- **Drop PDFs into `raw/` and run ingestion.** Don't manually summarize papers into wiki pages.
- **There are no per-paper pages.** Look for the concept (`REG_v1-layer4`, `PHE_orientation-tuning`).
- **Keep PDFs local.** `raw/` is excluded from git via `.gitignore`. Never commit PDFs to a shared repo. Only add papers you have legitimate access to. Because `raw/` is git-ignored, the `@` file picker will not list its contents. You need to type the path directly instead.
- **`†` means unverified against source.** If it matters for your work, add the PDF and run ingestion to promote it.
- **Don't edit pages manually** unless correcting a clear factual error. Add `<!-- QUERY: <concern> -->` and address it in the next agent session so the correction is sourced.
- **Check `wiki/index.md` first** before asking the agent to create a new page. The concept may already exist under a different slug.
- **Read VERIFICATION.md** before signing off on any session. Your sign-off is a meaningful attestation.
