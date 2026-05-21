# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Life-playbook** is a private personal knowledge base — a "playbook for life" stored as Markdown files. No build tools, package managers, or frameworks. Everything works in any Markdown viewer or directly on GitHub.

## Structure

```
index.md                        # Master table of contents — start here
principles.md                   # Core values and decision filter (the foundation)
health/                         # Fitness, sleep, nutrition protocols
career/                         # Work principles and financial rules
relationships/                  # How to show up for people
learning/                       # Reading system and skill-building framework
routines/                       # Daily anchors, weekly review, annual review templates
mental-models/                  # Decision-making frameworks
```

## Conventions

- **Each file follows the same pattern:** one-line purpose statement → principles/rules → protocols or templates where applicable.
- **Opinionated and personal.** This is a playbook, not a textbook — content should be direct and actionable, not general or hedged.
- **Cross-link liberally.** Use relative Markdown links (e.g. `[sleep protocol](../health/sleep.md)`) when one file references another.
- **index.md is the nav layer.** When adding a new file, add it to the table in `index.md`.

## When Adding Content

- Add new topics as new files in the relevant folder, or create a new folder if no existing area fits.
- Keep files focused — one topic per file.
- Update `index.md` to include any new files.
- Update this file if the folder structure changes significantly.
