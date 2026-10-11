---
name: echoes
description: Find a novel's lexical echoes and tics (a word repeated a few lines apart, a word dense over a passage, gesture verbs, weak verbs, -ment adverbs, tics across chapters), offer word alternatives the author chooses from, and prompts for the author's own images. Never rewrites a sentence.
disable-model-invocation: true
argument-hint: "[chapitres, ex. ch2 | ch1-ch3 | tout]"
---

# echoes

Version: 0.7.1 (author skills, see CHANGELOG)

Input: `NOVEL.md`, `bible/LEXICON.md` and `.echoes/intentional.md` if they
exist, the chapters named in the argument (ask if none). Output:
`.echoes/<chapter-id>.md`, then the word replacements the author chose,
per `validated-corrections`. Refuse to run without `NOVEL.md`: point to
`/setup-novel`.

This is style, the part `proofread` leaves out. The author's voice decides:
every row is `à confirmer`, alternatives are words or short noun phrases,
images are prompts. No sentence is written for the author.

## 1. Count

Run [the script](scripts/echoes.py) on the named chapters, plus every
other chapter for the cross-chapter tics:

```
python3 scripts/echoes.py manuscript/*.md --lexicon bible/LEXICON.md \
  --intentional .echoes/intentional.md --scene-break "* * *"
```

The path is relative to this skill's directory. It returns, per chapter:

- **echoes**: one word family twice or more within about 50 words;
- **concentrations**: one family four times or more within about 400
  words;
- **overuse**, **gestures** (regarder, s'arrêter, poser, se retourner…),
  **weak verbs** (faire, mettre, sembler, commencer à, chose) and
  **-ment adverbs** with their clusters;
- across chapters, **novel** tics: families dense in most chapters.

Families come from a light stemmer and can merge different words
(« porte », « porta »): the script finds candidates, it does not decide.
Lexicon terms are hidden only where they occur whole (« Porte des Brumes »
hides the place, not « la porte »); motifs are hidden by family.

## Deliberate echoes

`.echoes/intentional.md` has two sections, and the script reads only the
first:

```markdown
# Échos voulus

## Motifs
- brume — le brouillard du port, voulu

## Refusés
- ch4, l. 88 : « la lanterne éclairait à peine la lanterne voisine » — répétition voulue
```

- **Motifs**: one family per line, the word before « — », the reason
  after. The family is never counted again, in any chapter.
- **Refusés**: a row the author refused as deliberate, per
  `validated-corrections` (chapter id, line, extract, reason). The script
  still counts the word elsewhere; drop the candidate only where its extract
  is listed.

## 2. Judge

Read each candidate in its passage and keep it only when a reader would
feel the repetition. Drop it, with its reason in the report, when it is:

- a different word merged by the stemmer, or a word used in different
  senses (« foyer » the fire, « foyer » the home);
- the precise term with no equal (a technical word, a recurring object);
- a deliberate effect: anaphora, a refrain, a character's verbal tic in
  dialogue;
- an extract listed under `## Refusés`;
- a candidate motif: ask the author once (« “brume” revient 14 fois :
  motif voulu ? »); a yes goes under `## Motifs` and the family is never
  reported again.

For each kept echo, choose which occurrences to vary: usually not the
first, never the one where the word is the only right one.

## 3. Report

Write `.echoes/<chapter-id>.md`, replacing the previous report:

```markdown
# Échos ch4 — 2026-10-11
4 210 mots ; 6 échos retenus, 3 écartés ; tics : regard (6,2 ‰), s'arrêter (2,8 ‰)

## Remplacements

| ID | Ligne | Extrait | Correction | Raison | Certitude |
|---|---|---|---|---|---|
| E4-001 | 88 | « la lanterne éclairait à peine la lanterne voisine » | 1. « la lanterne éclairait à peine la lampe voisine » \| 2. « la lanterne éclairait à peine le fanal voisin » \| 3. « la lanterne éclairait à peine sa voisine » | écho : « lanterne » deux fois sur la ligne, 5 fois en 30 lignes | à confirmer |

## Tics

| Famille | Occurrences | Lignes | Piste |
|---|---|---|---|
| regard | 26 (6,2 ‰) | 12, 15, 31… | Que font les mains d'Aldric pendant qu'il écoute, au lieu de regarder ? |

## Pistes d'images
- l. 80–110, les lanternes : quel sens domine pour Mira ici, l'odeur de l'huile, le grésillement de la mèche ?

## Tics du roman
| Famille | ch3 | ch4 |
|---|---|---|
| regard | 4,1 ‰ | 6,2 ‰ |

## Écartés
- « port » (l. 40–52) : « porte » et « porta », deux mots fusionnés par le compteur.

## Hors périmètre
- l. 61 : « ils se sont assis » — temps composé dans un récit au passé simple, pour `proofread`.
```

- **Remplacements**: one row per occurrence to vary. **Correction** lists
  three to five numbered alternatives separated by `|`, each the whole
  extract with one word or short phrase changed (and the agreements that
  change requires), or the word removed when the sentence stands without
  it. Never abbreviate an alternative: it is applied as written.
  Alternatives fit the sense, the register and the world (the lexicon, the
  period).
- **Tics** (gestures, weak verbs, adverbs): no row, since varying a gesture
  means rewriting a beat. Each tic gets one prompt for the author, aimed
  at the passage where it is densest.
- **Pistes d'images**: for a concentration on a description, one or two
  questions that lead the author to their own image (a sense, a point of
  view, a comparison from the character's world). Never the image itself.

## 4. Validate and apply

Per `validated-corrections`, with ids `E<N>-<NNN>` and
`.echoes/intentional.md` (`## Refusés`). Every row has alternatives, so
the author answers each one by number or by their own word (`E4-001 : 2`,
`E4-003 : la veilleuse`).

## Done

Every candidate kept, dropped with its reason, or asked about as a motif;
every row applied, refused or listed as open.
