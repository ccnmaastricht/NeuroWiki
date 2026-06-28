# NeuroWiki

**This is a GitHub template repository.** Create one copy per project or research line. Click **Use this template** on GitHub, then follow the Quickstart below.

NeuroWiki is a modular LLM-agent system for building and maintaining citation-grounded knowledge bases in neuroscience. Papers go in; structured, synthesized, cross-linked wiki pages come out.

**[neurowiki.github.io](https://neurowiki.github.io)** · **[Example project wiki](https://github.com/MSenden/Example-Wiki)**

---

## What it does

- Reads PDFs and synthesizes their content into concept pages (phenomena, models, theories, brain regions, paradigms)
- Tracks citation provenance with a two-tier system: `(@Key)` for verified primary sources, `(@Key†)` for reconstructed secondary citations
- Surfaces conflicts between papers for human review rather than silently resolving them
- Maintains confidence levels (`established` / `debated` / `speculative`) on every page
- Supports structural harmonization, depth auditing, and cross-link auditing as independent refinement workflows
- Scales from a single project into a lab-level wiki via pull request submission to a lab wiki repository

## Repo layout

```
neurowiki/                     ← this template repo
├── README.md                  ← this file
├── CLAUDE.md                  ← Claude Code bootstrap → reads agent/AGENT.md
├── GEMINI.md                  ← Gemini CLI bootstrap → reads agent/AGENT.md
├── CURSOR.md                  ← Cursor bootstrap → reads agent/AGENT.md
├── AGENTS.md                  ← OpenAI Codex bootstrap → reads agent/AGENT.md
├── agent/                     ← agent instruction files
│   ├── AGENT.md               ← master agent file; read every session
│   ├── INGESTION.md           ← workflow: processing new PDFs
│   ├── REFINE_A.md            ← workflow: structural harmonization
│   ├── REFINE_B.md            ← workflow: depth audit
│   └── REFINE_C.md            ← workflow: cross-link audit
├── docs/                      ← human-facing documentation
│   ├── QUICKSTART.md          ← setup guide and session invocation prompts
│   ├── VERIFICATION.md        ← human verification protocol
│   ├── CONTRIBUTING.md        ← lab wiki submission guide
│   └── index.html             ← GitHub Pages landing page
├── scripts/                   ← tools
│   ├── validate.py            ← local pre-submission structural validation
│   ├── merge.py               ← lab wiki merge helper
│   └── setup.sh               ← one-command project initialization
├── .github/workflows/
│   └── validate.yml           ← CI: validates wiki structure on push
└── wiki/                      ← project wiki (empty; populated by agent)
    ├── primary.bib
    ├── secondary.bib
    ├── log.md
    ├── index.md
    └── pages/
```

## Quickstart

```bash
# 1. Use this repo as a GitHub template, then clone your new repo
git clone https://github.com/<you>/<your-project>
cd <your-project>

# 2. Initialize the wiki folder structure
bash scripts/setup.sh "My Project Name"

# 3. Fill in your project details
# Open agent/AGENT.md and complete Section 1

# 4. Add papers and start your first ingestion session
# Drop PDFs into raw/, then use a prompt from QUICKSTART.md
```

See **[QUICKSTART.md](docs/QUICKSTART.md)** for session invocation prompts and usage patterns.
See the **[example project wiki](https://github.com/MSenden/Example-Wiki)** for a populated wiki showing real pages, session logs, and refinement reports.

## Agent compatibility

NeuroWiki works with any LLM agent. Bootstrap files auto-load `AGENT.md` on launch for supported agents:

| Agent | Bootstrap file |
|-------|---------------|
| Claude Code | `CLAUDE.md` |
| Gemini CLI | `GEMINI.md` |
| Cursor | `CURSOR.md` |
| OpenAI Codex | `AGENTS.md` |
| Any other agent | Use invocation prompts from `QUICKSTART.md` |

## Ecosystem

NeuroWiki is the project layer of a two-tier local knowledge stack:

```
Lab wiki     ← lab level (separate repo; merges project wikis across a lab)
        ↑
NeuroWiki    ← project level (this repo)
```

When a project wiki is ready to share, it can be submitted to a lab wiki repository via pull request using the fork-copy-PR workflow described in **[CONTRIBUTING.md](docs/CONTRIBUTING.md)**. The lab wiki merges contributions from all projects within a lab into a unified synthesis.

## Legal notice

NeuroWiki produces scholarly synthesis from papers users have legitimately accessed. This is standard academic practice equivalent to writing a literature review or review article.

**PDFs and the `raw/` folder:**
- `raw/` is excluded from git tracking by default (via `.gitignore`, set by `setup.sh`). PDFs are never committed to any repository.
- Users are responsible for ensuring they have legitimate access to any PDF placed in `raw/` through institutional site licenses, open access, or author-provided copies.
- PDFs must never be committed to shared or public repositories, and are explicitly excluded from lab wiki submissions.

**Wiki pages:**
- The synthesized wiki pages are the user's own scholarly work. They paraphrase and cite sources; they do not reproduce substantial portions of copyrighted text.
- Users should ensure wiki pages do not quote excessively from any single source.

NeuroWiki does not endorse or facilitate copyright infringement. When in doubt, use open access sources (PubMed Central, bioRxiv, papers published under CC licenses).

## License

NeuroWiki uses a dual license reflecting the two distinct layers of the project:

| Layer | License |
|-------|---------|
| Infrastructure files (agent/AGENT.md, agent/INGESTION.md, agent/REFINE_*.md, scripts/validate.py, scripts/setup.sh, etc.) | Apache 2.0 with template exception |
| Wiki content (wiki/pages/, wiki/index.md, wiki/log.md, .bib files) | CC BY 4.0 |

**The template exception** means that using NeuroWiki to build a project wiki does not make your wiki a Derivative Work of NeuroWiki. Your wiki content is entirely your own — you may license it however you choose. The Apache 2.0 terms only apply if you distribute modified versions of the infrastructure files themselves.

**CC BY 4.0** on wiki content means anyone can reuse and build on the knowledge in the wiki as long as they credit the contributing lab(s). This is the standard license for open access scientific content.

See `LICENSE` (infrastructure) and `wiki/LICENSE` (content) for full terms.
