---
name: brainstorm
description: Frame a fuzzy story idea with the author (a scene, a plot turn, a character, a part of the world, an ending) until it holds, then write an idea brief. The agent suggests and challenges against canon; it never writes prose.
disable-model-invocation: true
argument-hint: "[l'idée, même floue]"
---

# brainstorm

Version: 0.7.1 (author skills, see CHANGELOG)

Input: `NOVEL.md`, the bible, the manuscript, the idea. Output:
`notes/ideas/<slug>.md`. Refuse to run without `NOVEL.md`: point to
`/setup-novel`.

For an idea that exists but will not take shape. When there is no idea at
all, `/muse` is the better tool: say so and stop.

## 1. Restate

Restate the idea in one sentence and name its kind (scène, retournement,
personnage, lieu, système, fin, structure). The author corrects the
sentence until it is theirs.

## 2. Context

Read what the idea touches: the sheets of the characters, places and
systems it involves, the chapters around where it would sit (a sub-agent
for a long manuscript). Collect the canon it must respect and the threads
it could pay off.

## 3. Converge

Run `grilling` in **suggest** mode on the idea's design tree: what is at
stake, who wants what, what changes after, where it sits, what the reader
knows. Where a branch is wide open, offer two or three contrasting
options, then let the author pick or reject them all.

Challenge against canon as you go: an option or answer that contradicts a
sheet, a ruling or the text is called out with its quote.

Suggestions are beats ("Mira trouve la lettre avant Aldric"), never prose:
no sentence, line of dialogue or description that could go into the novel.

## 4. Brief

When the frontier is empty and the author confirms the idea holds, write
the brief:

```markdown
# <Titre de l'idée>
date : 2026-10-09
type : <kind>

## Prémisse
<une phrase>

## Enjeu
## Déroulé
- <beat>
## Ce que ça change
- bible/characters/<slug>.md : <fait à ajouter ou modifier>
- ch<N> : <ce qui doit bouger dans le texte>
## Questions ouvertes
```

Sheet changes listed in **Ce que ça change** are proposals: apply one only
when the author asks, per `story-bible`.

## Done

The brief is written and every question left open is listed in it.
