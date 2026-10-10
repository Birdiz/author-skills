---
name: continuity-findings
description: Schema and rules for continuity findings in a novel (contradictions between chapters, or between the text and the bible). Use whenever writing, verifying or reading a file in .continuity/findings/.
---

# continuity-findings

Version: 0.3.0 (author skills, see CHANGELOG)

One file per axis, `.continuity/findings/<axis>.md`, kept across runs: a
finding is never deleted or renumbered, its fields change.

## Finding

A level-3 heading, a YAML block, three prose sections. YAML keys and section
titles stay in English; the prose is in the novel's language.

````markdown
### C-CHR-004 Couleur des yeux de Mira

```yaml
id: C-CHR-004
axis: characters        # characters | situations | world
kind: text-vs-bible     # see Kinds
impact: major           # major | minor
status: unverified      # unverified | confirmed | refuted
resolution: open        # open | bible-updated | text-corrected | ruled (R-…) | deferred
found: 2026-10-09
locations:
  - manuscript/03-la-fuite.md:41 « ses yeux verts »
  - manuscript/17-le-col.md:12 « ses yeux gris d'orage »
bible:
  - bible/characters/mira-valdane.md#Physique « Yeux : gris »
```

**Contradiction.** What the two sides state, in one or two sentences.

**Possible intent.** What could make it deliberate (a lie, a belief, time
passing, magic, a disguise), or "aucune".

**Resolutions.** The options the author can choose, the recommended one
first: update the sheet, correct the text (with the exact replacement),
record a ruling.
````

Every location carries its line and a verbatim quote: the author must be
able to check a finding without searching.

## Kinds

| Kind | Axis | Meaning |
|---|---|---|
| `text-vs-text` | any | two passages state incompatible facts |
| `text-vs-bible` | any | the text contradicts a sheet |
| `reveal-leak` | characters, world | the text states a `{secret}` or a fact before its `{révélé chN}` |
| `knowledge` | characters | a character uses what they cannot know yet |
| `skill` | characters | a character does what their savoir-faire excludes |
| `timeline` | situations | dates, durations, days and nights, seasons do not add up |
| `presence` | situations | a character in two places, or somewhere they cannot have reached |
| `travel` | situations | a journey faster than the distances table allows |
| `object` | situations | an object used after being lost, given or destroyed |
| `body` | situations | a wound, illness or fatigue that vanishes or changes |
| `rule` | world | a system used beyond its rules, costs or limits |
| `geography` | world | a place described against its sheet or its parent |
| `spelling` | world | a name outside the lexicon's term and variants |

## Impact

- `major`: an attentive reader would notice it, or it breaks the plot.
- `minor`: a detail few readers would catch. A conflict involving a fact
  marked `{à confirmer}` is always `minor`.

## IDs

`C-<AXIS>-<NNN>`: `CHR` characters, `SIT` situations, `WLD` world. Never
reused. Before adding a finding, search the file: a conflict already
recorded, at any status, gets a new location rather than a new finding.

## Status and resolution

`status` is set to `confirmed` or `refuted` only by verification, from a
context that did not write the finding. `resolution` is set only by the
author's arbitration. They are independent: a confirmed finding may be
`ruled` intentional.
