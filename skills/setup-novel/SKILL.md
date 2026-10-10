---
name: setup-novel
description: Configure a novel project once (manuscript layout, language, narrative tense and point of view, typography, proofreading tool, bible location). Run before any other novel skill, or when one reports a missing NOVEL.md.
disable-model-invocation: true
---

# setup-novel

Version: 0.5.0 (author skills, see CHANGELOG)

Write `NOVEL.md` at the root of the novel project. Talk to the author in
the language they write to you in, and once detected, the novel's. Every other skill refuses
to run without it. Run again to update it: read the existing file and ask
only about what changed or is missing.

## Process

1. **Detect the layout**: the Markdown chapter files (default
   `manuscript/*.md`), their order (file name), the chapter id rule (leading
   number → `ch<N>`), an existing bible, whether the project is a git
   repository, whether sub-agents are available. Paragraphs must be one per
   line: say so if the files are hard-wrapped.
2. **Detect from the text**: read the first, a middle and the last chapter.
   Infer the language, narrative tense, person, point of view, how dialogue
   is marked, and the typography in use: count `U+202F` and `U+00A0` before
   `; : ! ?`, `’` against `'`, `…` against `...`, `«` against `“`, `—`
   against `–` at the start of a line, and the scene-break marker (a
   short line of symbols alone between paragraphs).
3. **Detect the proofreading tool** (French only): look for Grammalecte's
   command line (`grammalecte-cli.py`) on PATH, then in the novel project
   (`find . -name grammalecte-cli.py`, a `tools/` directory is common) and
   under the home directory, before asking the author. Run it with `-h` and confirm it lists `-f`, `-j` (JSON) and
   `-on`/`-off`, `-lo`; when the installed version names them differently,
   record the equivalents in `NOVEL.md` next to the command. If absent,
   give the install steps: download the Python package from https://grammalecte.net
   ("Grammalecte pour Python"), unzip it, run
   `python3 grammalecte-cli.py -h`. Without it, `checker: none`.
4. **Confirm in rounds** with `grilling` in **suggest** mode, the detections
   as recommended answers. Each question takes its wording, definition,
   counter-example, examples and consequence from
   [questions](questions.md); a question with no reader is not asked.
5. **Write `NOVEL.md`** from [the template](novel-template.md).
6. **Offer to seed the lexicon**: list the capitalised words that recur
   mid-sentence in the manuscript, the author sorts them (character, place,
   invented word...) and gives gender and plural; write
   `bible/LEXICON.md` per `story-bible`. Skipping is fine: the build skills
   fill it later.

## Done

`NOVEL.md` written with no field left empty (a field the author does not
want is set to `none`), the checker command run once successfully or set to
`none`. Then list the next steps: `/build-character`, `/build-world`,
`/proofread <chapitre>`, `/check-continuity`.
