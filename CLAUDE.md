# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Life-playbook** is a private personal knowledge base — a "playbook for life" stored as Markdown files. No build tools, package managers, or frameworks. Everything works in any Markdown viewer or directly on GitHub.

## Structure

The playbook is organized conceptually by the **five layers** in `the-architecture.md`: Foundation → Operating System → Depth Work → Deployment → Synthesis. `index.md` mirrors those layers exactly. Folders are a storage convenience, not the taxonomy.

```
index.md                        # Master table of contents, grouped by the five layers — start here
the-architecture.md             # The five layers and how every file fits them (canonical taxonomy)
principles.md                   # Core values and decision filter (the foundation)
the-unit.md                     # Layer 5 synthesis doctrine
*.md (root)                     # Most topic files live at the root
about/                          # Who the playbook is built by
aspergers/                      # The Asperger's profile: energy, sensory, social decoding, work, user manual (Layer 1, "Wiring")
health/                         # Fitness, sleep, nutrition protocols
career/                         # Work principles and financial rules
relationships/                  # Relationship principles and intimate partnership
learning/                       # Reading system and skill-building framework
routines/                       # Daily anchors, weekly review, annual review templates
mental-models/                  # Decision-making, second-order, probabilistic thinking
tactics/                        # Social, field, cognitive, public speaking
```

## Conventions

- **Each file follows the same pattern:** one-line purpose statement → principles/rules → protocols or templates where applicable.
- **Opinionated and personal.** This is a playbook, not a textbook — content should be direct and actionable, not general or hedged.
- **Certainty is for values, not science.** Empirical claims (health, neuroscience, psychology research) carry an evidence tag: `[E: strong]` (consistent RCTs/meta-analyses), `[E: moderate]` (good observational data or small trials), `[E: weak]` (mechanism, animal data, or expert opinion), `[E: contested]` (serious evidence on both sides). Cite the study when giving a specific number. Values, rules, and protocols stay untagged and unhedged.
- **One canonical home per concept.** Before writing a concept that already exists elsewhere, link to it instead of restating it. Current canonical homes:
  - Dunbar's layers → `relationships/principles.md`
  - Moore & Gillette's four archetypes → `mythology-archetypes.md`
  - Second-order thinking → `mental-models/second-order-thinking.md`
  - Sleep science (light, temperature, caffeine timing) → `health/sleep.md`
  - The Asperger's profile — masking, burnout, sensory, double empathy, autism-specific social and work strategy → `aspergers/` (general social and work tactics stay in `tactics/social.md` and `career/work-principles.md`)
  - Values vs. rules of thumb vs. one-liners → `principles.md` / `heuristics.md` / `maxims.md` (principles wins conflicts)
- **Asperger's naming.** The section uses "Asperger's" deliberately: it names a distinct profile within autism, even though DSM-5 and ICD-11 merged the diagnoses. `aspergers/overview.md` explains the distinction and the name's history — keep that framing; never treat the distinction as a ranking.
- **Cross-link liberally.** Use relative Markdown links (e.g. `[sleep protocol](../health/sleep.md)`) when one file references another. Every file should have at least one inbound link besides `index.md`; files without a natural inline link get a `**Related:**` footer.

## When Adding Content

- Decide which of the five layers the topic belongs to before writing it.
- Add new topics as new files in the relevant folder, or at the root if no folder fits.
- Keep files focused — one topic per file.
- Add the file to the matching layer in **both** `index.md` and `the-architecture.md`.
- Link to it from at least one related file.
- Update this file if the structure or the canonical-home list changes.
