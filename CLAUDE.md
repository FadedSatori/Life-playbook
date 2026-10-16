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
