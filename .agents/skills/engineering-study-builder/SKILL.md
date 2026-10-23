---
name: engineering-study-builder
description: Master workflow that turns a folder of engineering documents (PDF, DOCX, Markdown, tables) into a source-traceable study package - source inventory, text/table/equation extraction, evidence matrix, cross-source synthesis, technical curriculum, textbook chapters, scientific and citation QA, and Markdown/DOCX/PDF export. Use when asked to build a study guide, technical textbook, training curriculum, or literature-based report from local engineering sources (semiconductor process, equipment, reliability, maintenance, cost). Every claim must resolve to a source ID plus locator. Runs fully local, no paid APIs.
license: MIT
compatibility: Python 3.10+ with pdfplumber, python-docx and reportlab (selftest only); pandoc, plus Chromium (preferred) or LibreOffice (soffice) for PDF export. No network and no API keys required. Reuses sibling skills markitdown, liteparse, literature-review, citation-management, scientific-writing, scholar-evaluation, scientific-critical-thinking, uncertainty-and-units, sympy, statistical-analysis, markdown-mermaid-writing and scientific-visualization when present.
allowed-tools: Read Write Edit Bash Glob Grep
metadata:
  version: "1.0"
  skill-author: local composition of K-Dense scientific-agent-skills
---

# Engineering Study Builder

Orchestrates existing skills around one rule: **no statement reaches the output without a path back to a source ID and locator**.

## Hard rules

1. Original files in `sources/` are never edited. Source IDs (`S001`...) are assigned by SHA-256, so duplicates collapse and later edits are detected.
2. Every factual, numeric or equation statement in a draft carries `[C###]` (evidence-matrix claim) or `[@S### locator]` (direct source cite, e.g. `[@S002 p.3]`, `[@S003 para 12]`, `[@S002 p.2 table 1]`).
3. Own derivations, assumptions and original examples are marked `{own}` and must show the derivation inputs (each input cited).
4. `direct` evidence needs a verbatim quote that is found at the locator. `derived`/`inferred` evidence needs a note explaining the step.
5. Never invent references, DOIs, page numbers or numbers. If a source does not say it, write "not stated in provided sources". When the answer is unknown, say "不知道".
6. Local tools only. Do not call paid or networked APIs. Skills that need the network (`paper-lookup`, `research-lookup`, `exa-search`, `parallel-web`, `paperclip`, `bgpt-paper-search`, `paperzilla`, `generate-image`, `infographics`) are out of scope unless the user explicitly adds web sources and accepts that.

## Workspace

```
study/
  sources/     originals (read-only)
  extracted/   S001.jsonl (text|table|equation blocks with locators), tables/*.csv
  ledger/      inventory.json, evidence.csv, reports/{matrix,qa}.json
  drafts/      synthesis.md, curriculum.md, ch01.md ...
  export/      <name>.md/.docx/.pdf
```

Driver: `python3 scripts/study.py --root study <command>` (path relative to this skill directory).

## Pipeline

| # | Phase | Command / reused skill | Gate |
|---|-------|------------------------|------|
| 1 | Ingest + inventory | `study.py init`, copy files into `sources/`, `study.py inventory`; fill `title`/`reliability` in `ledger/inventory.json`; for odd formats use **markitdown** (`batch_convert.py`) to produce `.md` first | Every source has an ID; unsupported files listed, not silently dropped |
| 2 | Extract PDF text, tables, equations | `study.py extract`; scanned PDFs (warning `no text layer`) go through **liteparse** OCR then re-inventory the output Markdown | Tables saved as CSV; equations captured with page; warnings reviewed |
| 3 | Evidence matrix | `study.py matrix-init`, add rows to `ledger/evidence.csv`, `study.py matrix` | Exit 0: every row resolves source, locator and verbatim quote |
| 4 | Cross-source synthesis | Write `drafts/synthesis.md` by topic: agreement, conflict, gap table; apply **scientific-critical-thinking** (bias, confounds, conditions) and **literature-review** structure (no network search); **scholar-evaluation** for developmental review of source quality (never to score people) | Conflicts show both claims with their IDs; gaps stated |
| 5 | Curriculum design | `drafts/curriculum.md`: audience, prerequisites, learning objectives (measurable verbs), module sequence, exercises, assessment; each module lists the claim IDs it teaches; **markdown-mermaid-writing** for dependency graphs | Each objective maps to >=1 claim ID and one exercise |
| 6 | Textbook chapters | One `drafts/chNN.md` per module following `references/chapter-template.md`; **scientific-writing** for prose standards; **scientific-visualization** + matplotlib for figures plotted from extracted CSV tables only | Figures cite the table source in the caption |
| 7 | Accuracy + citation QA | `study.py qa` (hard errors) then `study.py qa --strict` (warnings fail); **uncertainty-and-units** `audit_units.py`/`convert_units.py` for calculations; **sympy** to verify symbolic equations and dimensional consistency; **statistical-analysis** for statistics; **scientific-writing** `check_references.py`, `audit_claims.py` | See "QA checklist" |
| 8 | Export | `study.py export --name book --formats md docx pdf` (blocked if QA has errors); appends References built from inventory (ID, title, path, hash) | Output opened/size-checked; PDF via pandoc -> HTML (MathML) -> headless Chromium so equations render; LibreOffice fallback drops equations when libreoffice-math is missing; DOCX keeps native equations |

Sequential order matters: do not draft (4-6) before the matrix (3) passes, and do not export (8) before QA (7) has zero errors.

## Evidence matrix columns

`claim_id, claim, source_id, locator, quote, support(direct|derived|inferred), confidence(high|medium|low), note`

Locators are exactly as produced by extraction: `p.N`, `p.N table K`, `para N`, `table K`, `line N`. Matching of `p.2` also covers `p.2 table 1`.

## Synthesis rules (phase 4)

- Group claims by engineering question, not by document.
- For each question give: consensus (IDs), conflicts (with condition differences such as temperature, tool, recipe, unit basis), and unsupported gaps.
- Different units or bases are normalised with **uncertainty-and-units**, with the conversion shown. Never silently average values from different conditions.
- Rate source strength (primary data > standard/spec > vendor note > secondary summary) in `inventory.json` `reliability`.

## QA checklist (phase 7)

1. `matrix` and `qa` exit 0; `unused_sources` in `reports/qa.json` reviewed (intentionally unused or missing coverage).
2. Warnings cleared: each uncited numeric statement is cited or marked `{own}` with inputs.
3. Every equation: symbols defined, units consistent (sympy/pint), source or `{own}` derivation.
4. Every number in prose equals the extracted table value (spot-check 10% minimum, all headline numbers).
5. Claims are not stronger than the quote (scope, conditions, sample size preserved).
6. Terminology consistent across chapters; abbreviations defined at first use.
7. Run `python3 scripts/selftest.py` after modifying the scripts.

## Failure handling

- Locator not found: re-open the extracted block, fix the locator; do not edit the quote to match.
- Source changed after inventory: `extract` warns; re-run `inventory` (new hash gets a new ID) and re-check dependent claims.
- Missing optional tools: pdfplumber absent -> use **liteparse**/**markitdown**; pandoc absent, or neither Chromium nor soffice -> deliver Markdown and say which formats were not produced.

## Verification

`python3 scripts/selftest.py` builds synthetic PDF/DOCX/Markdown sources, runs phases 1-3, 7, 8, and checks that fabricated quotes, bad locators, unknown sources, missing notes and uncited numbers are all rejected.
