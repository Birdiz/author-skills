# Changelog

File formats (`NOVEL.md`, bible files, facts, findings, proofreading
reports) are a public interface: a change to one is listed here.

## 0.6.1 (2026-10-11)

`validated-corrections`: a skill proposes corrections only within its own
scope. `scene-breaks` proposed two continuity fixes without extraction,
verification or arbitration; out-of-scope observations now go into a
`## Hors périmètre` section of the report, for the owning skill.

## 0.6.0 (2026-10-11)

From the second proofreading run:

- A construction error that no word replacement fixes gets the smallest
  rewording of its clause, `à confirmer`, with a **Règle** starting with
  `reformulation :`. ADR 0003 is amended to allow it.
- Comparisons between terms that do not compare are in scope, `à
  confirmer`.

## 0.5.1 (2026-10-11)

`validated-corrections` applies rows from the last line to the first, so
rows that split a paragraph or remove a scene break keep the other rows'
line numbers valid. The first 0.5.0 run did it right without the rule.

## 0.5.0 (2026-10-11)

- **New `NOVEL.md` field** `scene_break` (default `"* * *"`). Add it to
  an existing `NOVEL.md`, or run `/setup-novel` again.
- **New skill `scene-breaks`**: keeps, removes or adds scene-break markers,
  each change validated by the author. Report `.scenes/<chapter-id>.md`.
- **New skill `validated-corrections`**: the one protocol for changing the
  manuscript (rows, certainty, validating answers, applying, deliberate
  forms), used by `proofread`, `scene-breaks` and `check-continuity`.
- **`proofread` reads more thoroughly**: typography by a deterministic
  script (`scripts/typography.py`), then batches of about fifteen
  paragraphs read twice, once for language (A) and once for punctuation
  and dialogue (B), with coverage checked. Scope now names detached
  participles, *si* + conditional, missing words, vocative commas and
  narration glued to a reply. **Report format**: new `Source` column.
- Fact extracts record scene breaks and what changes across them.

## 0.4.0 (2026-10-10)

Fixes from the first real `proofread` run:

- **Report format.** Certainty values are `certaine` | `à confirmer`
  (was `certain`). Typography forms ruled out by `NOVEL.md` get one row
  per rule with its count.
- Validation answers are `tout` (every row), `les certaines`, ids, ranges,
  `tout sauf …`. `tout certain` is gone: an author read it as "all of
  it", the skill as "only the certain rows". Only these forms validate; a
  question is answered and the choice offered again. Before applying, one
  line says what is applied and what stays open.
- The checker's options are turned off for typography the author chose
  against its rules (an ordinary space before `; : ! ?`), not only for
  `ignore`.
- Skills address the author as the author addresses them (tu or vous).

## 0.3.1 (2026-10-10)

Fixes from the first real `setup-novel` run:

- `grilling`: a manuscript example is quoted after re-reading its
  surroundings, up to the end of the reply it cites; examples illustrate a
  setting with an imagined change and never present an existing passage as
  a contradiction (an example claimed one that a reply two words later
  resolved).
- Free indirect style is recorded as the character's thought in fact
  extracts and considered at verification; `questions.md` explains it.
- `setup-novel` searches the project and home directory for Grammalecte
  before giving install steps.
- Every message to the author is in the novel's language.

## 0.3.0 (2026-10-10)

`grilling` defines every notion it asks about (definition, what it is not,
an example, what the answer changes), answers the author's questions back
before asking again, and takes examples only from the manuscript (quoted)
or from a skill's reference. `setup-novel` asks from a new reference,
`questions.md`, with vetted examples. No format change.

## 0.2.0 (2026-10-10)

**Breaking (`NOVEL.md`).** `unreliable_narrator: no | <names>` becomes
`misleading_narration: [<names>]`, `[]` when the narration is always true.
`setup-novel` asks « La narration fait-elle foi ? » instead of a negated
question. To migrate, replace `unreliable_narrator: no` with
`misleading_narration: []`, or list the same names.

`grilling` asks every question in the positive.

## 0.1.0 (2026-10-09)

First version of every skill: `setup-novel`, `proofread`,
`build-character`, `build-world`, `check-continuity`, `brainstorm`, `muse`,
`story-bible`, `grilling`, `continuity-findings`. Not yet run on a real
manuscript.
