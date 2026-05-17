# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Life-playbook** is a personal repository owned by **Levi Satori (FadedSatori)**. Based on its name and description ("Playbook for life"), this is intended to be a collection of personal guidelines, principles, habits, goals, processes, or reference material — essentially a living document or set of documents that the owner uses to guide their life.

The repository is in its earliest stage (single initial commit with only a README).

## Repository Structure

```
Life-playbook/
└── README.md   — project description ("Playbook for life")
```

As content is added, this section should be updated to reflect new files and directories.

## Build / Test / Run

There is nothing to build, test, or run. This is a documentation/content repository. No package manager, compiler, or test framework applies.

## Development Workflow

- **Default branch:** `main`
- **Branch strategy:** Standard GitHub flow — create a branch, make changes, open a PR to `main`, merge
- **Claude-generated branches** follow the pattern `claude/<purpose>-<id>`

## Key Conventions

- **Content format:** All content is expected to be Markdown (`.md` files). Do not introduce code files, build tooling, or application scaffolding unless explicitly requested.
- **File organisation:** As content grows, group related documents into subdirectories (e.g. `habits/`, `goals/`, `principles/`, `templates/`). Only create structure when there is content to put in it.
- **Editing style:** Write clearly and personally — this is a personal playbook, not a technical spec. Plain English, first-person where appropriate.
- **Do not fabricate content** about the owner's life, goals, or values. Only add content the owner provides or requests.
- **Keep commits descriptive** — commit messages should clearly state what section or document was added/changed.

## Context for AI Assistants

- Owner: FadedSatori (Levi Satori)
- Primary language: Markdown only
- No secrets, environment variables, or external integrations
- This repository is intentionally personal — treat its contents with appropriate discretion
- When asked to add content, ask clarifying questions if the intent is unclear rather than guessing
