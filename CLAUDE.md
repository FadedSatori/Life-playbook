# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Life-playbook** is a private personal knowledge base — a "playbook for life" stored as Markdown files. No build tools, package managers, or frameworks. Everything works in any Markdown viewer or directly on GitHub.

## Structure

```
index.md                        # Master table of contents — start here
principles.md                   # Core values and decision filter (the foundation)
the-architecture.md             # How all files connect (update when adding major files)
about/                          # Who the playbook is by and why
tactics/                        # Social, field, cognitive, public speaking
health/                         # Fitness, sleep, nutrition protocols
career/                         # Work principles and financial rules
relationships/                  # How to show up for people, intimate partnership
learning/                       # Reading system and skill-building framework
routines/                       # Daily anchors, weekly review, annual review templates
mental-models/                  # Decision-making, second-order, probabilistic thinking
*.md (root)                     # Topic files: one subject each (e.g. warfare.md,
                                #   attention.md, negotiation.md, sales.md,
                                #   wealth-building.md, dark-psychology.md,
                                #   counter-strategies.md, purpose.md, time.md, ...)
```

Root-level topic files are grouped into sections in `index.md` (Operator, Depth, Next-Gen, Transcendent, Ancient & Legendary, etc.). Check `index.md` for the current full list rather than relying on this tree.

## Conventions

- **Each file follows the same pattern:** one-line purpose statement → principles/rules → protocols or templates where applicable.
- **Opinionated and personal.** This is a playbook, not a textbook — content should be direct and actionable, not general or hedged.
- **Cross-link liberally.** Use relative Markdown links (e.g. `[sleep protocol](../health/sleep.md)`) when one file references another.
- **index.md is the nav layer.** When adding a new file, add it to the table in `index.md`.

## When Adding Content

- Add new topics as new files in the relevant folder, or create a new folder if no existing area fits.
- Keep files focused — one topic per file.
- Update `index.md` to include any new files.
- Update `the-architecture.md` when adding a major new file so the system map stays current.
- Update this file if the folder structure changes significantly.
- Verify factual claims, numbers, and attributions before writing them in. Prefer named, checkable sources; flag anything uncertain rather than inventing precision.
- Read `HANDOFF.md` at the start of a session for the current state, open items, and known unverified claims.

## Accuracy Standards

Two fact-check passes found roughly 250 errors in earlier content. Hold new writing to these rules:

1. **Name only real, correctly attributed sources.** Researcher + year in prose; no URLs or footnotes in the text. Give a year or number only when sure; prefer "about" or "roughly."
2. **Quotation marks only for verified wording.** Otherwise paraphrase. Popular internet quotes credited to Einstein, Churchill, Lincoln, Marcus Aurelius, Bruce Lee, Jung, and similar figures are often fake; mark them "attributed (unverified)" or find the real source.
3. **Flag contested and failed-to-replicate findings.** Known problem claims, already corrected in the repo, include power-posing hormones, ego depletion, 10,000 hours as a threshold, Mehrabian's 7-38-55 as a general rule, the backfire effect as common, "21 days to form a habit" (Lally 2010: median about 66), the Zeigarnik memory effect, Ward 2017 phone presence, MBTI validity, and lie detection by cues (about 54% accuracy). Don't reintroduce them.
4. **Health, legal, safety, and financial content** stays conservative, general, and points to professionals. Crisis lines and hotlines must be verified; they change (1-800-GAMBLER was reassigned in 2025).
5. **Don't revert earlier corrections.** Wording such as "attributed to," "paraphrase," "unverified," "observational," and "in mice" is deliberate.
6. **Defensive framing** for the intelligence, manipulation, and security files: recognize, resist, report. No how-tos for surveilling, tracking, deceiving, or harming people.

## Working Notes for Claude Sessions

- **Personal files:** don't rewrite `about/levi-satori.md` or `principles.md` without the owner asking; propose edits instead.
- **Web access:** WebSearch works; WebFetch and direct HTTP to most hosts are blocked by this environment's network policy, so the `deep-research` workflow returns nothing. Use agents with WebSearch instead. Web searches share a budget of about 200 per turn across all agents.
- **Workflow that works:** parallel agents for writing or checking, each owning separate files; review every diff yourself before committing; commit per group with a descriptive message.
- **Before every commit**, check that relative links resolve:

  ```bash
  find . -name '*.md' -not -path './.git/*' -not -name CLAUDE.md | while read f; do d=$(dirname "$f"); grep -o '\]([^)#]*\.md[^)]*)' "$f" | sed 's/^](//; s/)$//; s/#.*//' | sort -u | while read l; do [ -f "$d/$l" ] || echo "BROKEN in $f: $l"; done; done
  ```
