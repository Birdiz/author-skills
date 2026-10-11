---
name: build-character
description: Build or deepen a character sheet with the author, in two phases (core questions from the template, then physique, psychology, savoir, savoir-faire, savoir-être, voice, relations, arc). The agent asks; the author decides.
disable-model-invocation: true
argument-hint: "[nom du personnage]"
---

# build-character

Version: 0.7.0 (author skills, see CHANGELOG)

Input: `NOVEL.md`, the bible, the manuscript. Output:
`bible/characters/<slug>.md` and its lexicon entries, per `story-bible`.
Refuse to run without `NOVEL.md`: point to `/setup-novel`.

The character is the author's: `grilling` runs in **ask** mode throughout.
The [template](../story-bible/character-template.md) holds the sheet and
the questions.

## 1. What is already canon

If a sheet exists, read it. Search the manuscript for the name and its
variants from the lexicon (a sub-agent when the manuscript is long): every
fact the text states about the character, with chapter, line and quote.
Show the author what the text establishes and any conflict with the sheet;
a conflict is settled now, per `story-bible`'s canon rule, before any new
question.

## 2. Phase 1: socle

Ask the phase 1 questions the sheet and the text leave open, in rounds.
Write the sheet after each round, and add the name, surnames and variants
to `LEXICON.md` with gender. Phase 1 is done when every question is
answered or `{à décider}`.

## 3. Phase 2: approfondissement

Offer the dimensions (physique, psychologie, savoir, savoir-faire,
savoir-être, voix, relations, arc détaillé) and let the author pick any,
all, or none. For each picked dimension, ask its questions in rounds and
write as you go. Push for what makes the sheet checkable: when a trait
changes during the novel, its chapter (`{dès chN}`); when the reader must
not know it yet, its reveal (`{secret}`, `{révélé chN}`); for each
savoir-faire, its level and its limit.

A relation written on this sheet is a fact about two characters: when the
other one has a sheet, add the matching line there too, in the same edit.

## Done

The sheet holds every answer given, with annotations; the lexicon has every
name; no phase 1 question is open. Summarise in five lines what the sheet
now establishes, and list the `{à décider}` left.
