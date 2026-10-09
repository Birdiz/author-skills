# Lexicon, timeline and rulings

## LEXICON.md

One table, sorted alphabetically. The gender and plural of an invented word
are what lets `proofread` check its agreements.

```markdown
# Lexique

| Terme | Catégorie | Genre | Pluriel | Variantes admises | Fiche |
|---|---|---|---|---|---|
| Mira Valdane | personnage | f | — | Mira, la Valdane | characters/mira-valdane.md |
| ombrelin | espèce | m | ombrelins | Ombrelin (en début de phrase) | world/systems/ombrelins.md |
| Valmont | ville | f | — | — | world/places/valmont.md |
```

Catégories: `personnage`, `lieu`, `système`, `mot inventé`, `titre`,
`juron`, `autre`. A spelling outside `Terme` and `Variantes admises` is
an error for `proofread` and a finding for `check-continuity` (world axis).

## timeline.md

The author's chronology, in the world's calendar, including events before
the novel. Sorted by date.

```markdown
# Chronologie

Calendrier : [<nom>](world/systems/<slug>.md)

| Date | Événement | Chapitre | Personnages | Lieu |
|---|---|---|---|---|
| An 320 | Chute de Valmont | — | Aldric (enfant) | Valmont |
| An 342, 3 printemps | Mira quitte le Gué | ch1 | Mira | Le Gué |
```

## rulings.md

One entry per ruling, newest last, ids never reused.

```markdown
# Décisions de canon

### R-007 Mira ment sur son âge (ch4)
- date : 2026-10-09
- source : C-CHR-012
- décision : intentionnel, elle se vieillit pour être engagée.
- portée : ch4, l. 33 seulement ; toute autre mention suit la fiche.
```

A ruling has a scope: the lines or chapters it covers. A check suppresses
a conflict only inside that scope.
