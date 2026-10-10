# Changelog

File formats (`NOVEL.md`, bible files, facts, findings, proofreading
reports) are a public interface: a change to one is listed here.

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
