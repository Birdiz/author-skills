---
name: story-bible
description: Format and rules of a novel's bible (character, place and system sheets, lexicon, timeline, canon rulings, fact annotations). Use whenever reading or writing a bible file, or comparing the manuscript with canon.
---

# story-bible

Version: 0.5.1 (author skills, see CHANGELOG)

The bible is the canon outside the text. Its path is `bible.path` in
`NOVEL.md` (default `bible/`).

## Layout

```
bible/
├── LEXICON.md
├── characters/<slug>.md
├── world/
│   ├── places/<slug>.md
│   └── systems/<slug>.md
├── timeline.md
└── rulings.md
```

`<slug>`: the canonical name, lowercase, ASCII, hyphens (`mira-valdane`).
Create files lazily, when there is something to write. Templates:
[character](character-template.md), [place](place-template.md),
[system](system-template.md). Lexicon, timeline and rulings:
[formats](formats.md).

## Rules

- **Single source of truth.** A fact lives in one sheet; other sheets link
  to it (`[Valmont](../world/places/valmont.md)`). A place names its
  parent, never its children: children are found by search.
- **Write facts, not prose.** Short lines, the author's words when they gave
  them. A sheet is reference, not a draft of the novel.
- **Every name in the lexicon.** A new character, place, system or invented
  word goes into `LEXICON.md` with its gender and plural in the same edit.
- **Annotate time and reveals.** A fact without annotation is true for the
  whole novel and may be stated anywhere. Otherwise:

| Annotation | Meaning | What a check does with it |
|---|---|---|
| `{dès ch12}` | true from chapter 12 | text before ch12 stating it: finding |
| `{jusqu'à ch8}` | true up to chapter 8 included | text after ch8 stating it: finding |
| `{secret}` | the author's knowledge only | text stating it: reveal leak |
| `{révélé ch20}` | the reader learns it in ch20 | text before ch20 stating it: reveal leak |
| `{croyance: <qui>}` | believed by these characters, not necessarily true | never contradicts a true fact |
| `{à confirmer}` | the author is unsure | conflicts reported as low impact |
| `{à décider}` | not decided yet | never compared |

Annotations combine: `- Boite de la jambe gauche {dès ch12}`.

## Canon

The bible and the manuscript are both canon; when they disagree, neither
wins. Raise the conflict to the author with both quotes and apply their
choice: update the sheet, apply a correction to the text after validation,
or add a ruling. Rulings in `rulings.md` override both for their scope.
