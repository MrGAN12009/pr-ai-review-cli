# PR AI Review CLI

A tiny command-line notes app for teaching pull requests and AI-assisted code review.

The project is intentionally small: students can understand the full codebase in a few minutes, then practice reviewing focused changes.

## Features

- Add short notes.
- List saved notes.
- Clear all notes.
- Store data in a local JSON file.

## Usage

Run the CLI with Python:

```bash
python note_cli.py add "Remember to write a useful PR description"
python note_cli.py list
python note_cli.py clear
```

By default, notes are stored in `.notes.json`.

You can also use a separate notes file for experiments:

```bash
python note_cli.py --store demo-notes.json add "Open a pull request"
python note_cli.py --store demo-notes.json list
```

## Quick Review Checklist

Before opening a pull request, check:

- the command still runs;
- the diff contains only lesson-related changes;
- the PR title says what changed;
- the PR description explains how to test the change.

## Lesson Flow

This repository is prepared for a lesson about:

- creating a feature branch;
- opening a pull request;
- asking AI to review a diff;
- deciding which AI comments are useful;
- pushing fixes to the same PR.

Merge conflicts are intentionally out of scope for this lesson.

## Demo Branches

Three pull requests are already prepared.

Two extra branches are pushed without pull requests so they can be used during a live demo:

- `lesson/add-note-count`
- `lesson/add-export-command`


Этот проект является учебным и не подлежит использованию!