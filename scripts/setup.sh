#!/usr/bin/env bash
# NeuroWiki project setup script
# Usage: bash scripts/setup.sh "My Project Name"
# Run this once in the root of a new project folder.

set -e

PROJECT_NAME="${1:-My NeuroWiki Project}"

echo "Setting up NeuroWiki project: $PROJECT_NAME"

# Create directory structure
mkdir -p raw wiki/pages

# Ensure raw/ is excluded from git via .gitignore
grep -q "^raw/$" .gitignore 2>/dev/null || echo "raw/" >> .gitignore
echo "raw/ excluded from git tracking (via .gitignore)"

# Propagate project name into agent/AGENT.md
if grep -q "^Project name:" agent/AGENT.md 2>/dev/null; then
    sed -i "s|^Project name:.*|Project name:             ${PROJECT_NAME}|" agent/AGENT.md
    echo "agent/AGENT.md project name set to: $PROJECT_NAME"
fi

# Initialize wiki files
cat > wiki/primary.bib << 'BIBEOF'
% primary.bib — papers with PDFs in raw/
% Managed by NeuroWiki agent. Do not edit manually.
BIBEOF

cat > wiki/secondary.bib << 'BIBEOF'
% secondary.bib — papers cited within PDFs but not held locally
% Entries marked with: note = {reconstructed from @SourceKey}
% Managed by NeuroWiki agent. Do not edit manually.
BIBEOF

cat > wiki/log.md << 'LOGEOF'
# Session Log

One entry per agent session. Each entry signed off by a lab member after verification.
See docs/VERIFICATION.md for the verification protocol.

---
LOGEOF

# Seed wiki/index.md
cat > wiki/index.md << INDEXEOF
---
type: index
title: Wiki Root Index
updated: $(date +%Y-%m-%d)
---

# Wiki Index — ${PROJECT_NAME}

## Phenomena
| Page | Title | Confidence | Updated |
|------|-------|------------|---------|

## Models
| Page | Title | Confidence | Updated |
|------|-------|------------|---------|

## Methods & Analysis
| Page | Title | Confidence | Updated |
|------|-------|------------|---------|

## Theories
| Page | Title | Status | Updated |
|------|-------|--------|---------|

## Brain Regions & Cell Types
| Page | Title | Confidence | Updated |
|------|-------|------------|---------|

## Paradigms & Datasets
| Page | Title | Updated |
|------|-------|---------|
INDEXEOF

echo ""
echo "Done. Next steps:"
echo "  1. Open agent/AGENT.md and complete the remaining fields in Section 1 (research question, brain regions, theories, etc.)"
echo "  2. Add PDFs to raw/ (never committed to git — excluded via .gitignore)"
echo "  3. Start an ingestion session using a prompt from docs/QUICKSTART.md"
echo ""
echo "Folder structure created:"
find wiki raw -type f | sort
