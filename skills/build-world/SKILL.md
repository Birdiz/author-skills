---
name: build-world
description: Build or deepen a world sheet with the author, a place at any scale (building, district, village, city, region, country, continent, world) or a system (magic, faction, religion, technology, species, language, calendar, economy, past event), with optional deepening. The agent asks; the author decides.
disable-model-invocation: true
argument-hint: "[nom du lieu ou du système]"
---

# build-world

Version: 0.3.1 (author skills, see CHANGELOG)

Input: `NOVEL.md`, the bible, the manuscript. Output:
`bible/world/places/<slug>.md` or `bible/world/systems/<slug>.md`, lexicon
entries, and timeline entries, per `story-bible`. Refuse to run without
`NOVEL.md`: point to `/setup-novel`.

The world is the author's: `grilling` runs in **ask** mode throughout.

## 1. Place or system

Ask which, unless the existing sheet or the name settles it: a closed
choice. For a place, ask its scale and its parent; a parent with no sheet
gets a stub (name, scale, its own parent) so the chain stays whole. For a
system, ask its type.

Templates: [place](../story-bible/place-template.md),
[system](../story-bible/system-template.md).

## 2. What is already canon

If a sheet exists, read it. Search the manuscript and the other sheets for
the name and its variants (a sub-agent when the manuscript is long): every
stated fact, with chapter, line and quote. Show the author what is
established and any conflict; a conflict is settled now, per
`story-bible`'s canon rule, before any new question.

## 3. Core

Ask the core questions and those of the scale or type that the sheet and
text leave open, in rounds; write the sheet after each round, the name and
invented words into `LEXICON.md` with gender and plural, dated events into
`timeline.md`.

Push for what makes the sheet checkable:

- a place: distances and travel times to the other places of the story;
- a system: costs and limits before powers, and what people believe
  (`{croyance: <qui>}`) apart from what is true.

The core is done when every core question is answered or `{à décider}`.

## 4. Approfondissement (optional)

Offer the template's deepening topics; the author picks any or none. Ask
and write as in step 3.

## Done

The sheet holds every answer given, with annotations; lexicon and timeline
are updated; the parent chain of a place is whole. Summarise in five lines
what the sheet now establishes, and list the `{à décider}` left.
