# Fact extraction

Read one chapter in full and write `.continuity/facts/<chapter-id>.md`. The
facts file replaces the chapter for every comparison: a fact left out is a
contradiction nobody will find.

## Rules

- **Every fact carries its line and a short verbatim quote.**
- **Record the source**: `narration`, `dialogue: <who>`, `pensée: <who>`,
  `lettre: <who>`... A character's statement is recorded as their
  statement, never as a fact of the world. Free indirect style (the
  narration voicing a character's thought without a verb of thinking) is
  `pensée: <who>` when the context marks it as theirs.
- **Facts, not judgements.** No interpretation, no comparison with other
  chapters or the bible.
- **Names in canonical form** from the lexicon, with the form used in the
  text when it differs.
- **Scene breaks** (`scene_break` in `NOVEL.md`): each marker with what
  changes across it, as the text states it.
- Exhaustive within the sections below; nothing outside them.

## Format

```markdown
---
chapter: ch3
file: manuscript/03-la-fuite.md
hash: <git hash-object>
extracted: 2026-10-09
pov: Mira
---

## Scènes
- l.39 « * * * » → lieu : forêt → Vieux-Gué ; temps : même soir

## Temps
- l.1 narration « Trois jours après l'incendie » → début : incendie + 3 jours
- l.40 narration « la nuit tombait » → soir

## Lieux et déplacements
- l.5 narration Mira, Aldric : auberge du Gué
- l.88 narration Mira, Aldric partent pour Valmont, à cheval

## Personnages
- Mira, l.41 narration « ses yeux verts » (physique)
- Mira, l.60 dialogue: Aldric « je suis le fils du roi » → Mira l'apprend ici (savoir)
- Aldric, l.72 narration crochète une serrure (savoir-faire)

## Objets
- l.20 narration l'épée d'Aldric tombe dans la rivière (perdue)

## Corps
- l.70 narration Mira blessée à l'épaule gauche

## Monde
- l.33 dialogue: aubergiste « Valmont est à deux jours de cheval »
- l.50 narration Mira use du feu des braises, puis fièvre (coût) → système: feu-des-braises
- l.55 narration « Ombrelins » (orthographe dans le texte)

## Révélations
- l.60 le lecteur apprend : Aldric est le fils du roi
```
