---
name: scene-breaks
description: Check where a novel's chapters break into scenes, propose removing scene-break markers that cut a continuous scene and adding the missing ones, and apply only what the author validates.
disable-model-invocation: true
argument-hint: "[chapitres, ex. ch1 | ch1-ch3 | tout]"
---

# scene-breaks

Version: 0.7.2 (author skills, see CHANGELOG)

Input: `NOVEL.md` (`scene_break`, the marker line), the chapters named in
the argument (ask if none), `.scenes/intentional.md` if it exists.
Output: `.scenes/<chapter-id>.md`, then the validated changes per
`validated-corrections`. Refuse to run without `NOVEL.md`: point to
`/setup-novel`.

The marker matters beyond layout: `check-continuity` reads each one as a
possible jump in time or place.

## What a scene break is

A break in the continuity of the story, on at least one of:

- **time**: an ellipsis (« Le lendemain matin », « Trois jours plus
  tard »), or a return to an earlier moment;
- **place**: the story is somewhere else without following a character
  there;
- **point of view**: another character's perception takes over;
- **thread**: the story cuts to other characters elsewhere.

Not a scene break: a pause in the action, a beat between two replies, a
description or a reflection inside the same moment, a change of subject in
the same place and moment, a character walking from one room to the next
while the story follows.

## 1. Read

Read the whole chapter. For every marker, decide **keep** or **remove**;
for every paragraph boundary without one, decide whether a marker is
**missing**. Each decision names the criterion (time, place, point of
view, thread, or "continuité") and quotes the end of the paragraph before
and the start of the paragraph after.

Certainty, per `validated-corrections`: `certaine` when the text states the
change (« Le lendemain ») or the continuity (a reply to the question just
asked); `à confirmer` otherwise.

## 2. Report

Write `.scenes/<chapter-id>.md`, replacing the previous report:

```markdown
# Scènes ch4 — 2026-10-10
Marqueur : « * * * » ; 6 présents, 2 conservés, 4 à retirer, 1 à ajouter

| ID | Ligne | Extrait | Correction | Raison | Certitude |
|---|---|---|---|---|---|
| S4-001 | 25 | « …frappa deux coups. ⁂ — Entrez ! » | retirer le marqueur | continuité : la réplique répond aux coups frappés | certaine |
| S4-002 | 61 | « …et s'endormit. ⁂ Le lendemain, » | ajouter le marqueur avant la ligne 61 | temps : « Le lendemain » | certaine |

## Conservés
- l. 39 : lieu, la ferme → le port (« …referma la barrière. » / « Sur les quais, »)
```

`⁂` in an extract marks the boundary. Kept markers are listed with their
reason so the author sees the whole cut.

## 3. Validate and apply

Per `validated-corrections`, with ids `S<N>-<NNN>` and
`.scenes/intentional.md`. A removal deletes the marker line and one of the
blank lines around it; an addition inserts the marker on its own line with
a blank line on each side. Apply from the last line of the chapter to the
first, so the line numbers of the rows still to apply stay right.

## Done

Every marker kept or decided on, every missing break proposed, every row
applied, refused or listed as open.
