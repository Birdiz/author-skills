---
name: grilling
description: Interview the author in rounds until every branch of a character, place, system, idea or setup decision is resolved. Use when a novel skill needs the author's decisions, in ask mode (questions only) or suggest mode (each question with a recommended answer).
---

# grilling

Version: 0.6.1 (author skills, see CHANGELOG)

The interview primitive behind `setup-novel`, `build-character`,
`build-world`, `brainstorm` and `check-continuity`'s arbitration. Adapted
from [mattpocock/skills](https://github.com/mattpocock/skills)' `grilling`.

## Mode

The calling skill names the mode:

- **ask**: for creative decisions the author owns (who a character is, what
  a place looks like). Ask open questions. Options are allowed only when
  they enumerate a closed set (POV or not; a scale; a system type), never
  creative content. If the author asks for ideas, give three contrasting
  ones for that question only, then return to ask mode.
- **suggest**: for framing and setup decisions. Give each question a
  recommended answer, worded so that "oui" accepts it.

Word every question in the positive: « La narration fait-elle foi ? »,
not « Le narrateur est-il non fiable ? ». A negated question makes "non"
mean yes, and the author answers the opposite of what they mean.

## Answerable questions

- **Define the notion.** A question resting on a literary or technical
  notion (narration qui fait foi, focalisation, concordance des temps)
  carries, in the question itself, a one-line definition, what it is not,
  one example, and what the answer changes. The calling skill's reference
  is the source when it has one.
- **Examples are claims.** An example from the manuscript is quoted with
  chapter and line, after re-reading the paragraphs around it: the quote
  holds the whole exchange, up to the end of the reply it cites. It is
  checked against the definition before it is shown: a thought reported as
  a thought, or a lie in dialogue, is not narration.
- **Illustrate, do not diagnose.** To show what a setting changes, pair a
  real quote with an explicitly imagined change (« Imagine qu'un ch6
  écrive… »). A statement that the text already contradicts itself is a
  finding: it belongs to `check-continuity`, with its verification.
- **Published works** come only from the calling skill's reference. With
  neither source, say there is no example in the text yet.
- **A question back comes first.** When the author answers with a question
  (what it means, an example, a consequence), answer it fully, then ask
  again with the answer folded in.

## Rounds

Map the subject as a **design tree**: each decision branches into the ones
that hang off it. The **frontier** is every open decision whose
prerequisites are settled.

1. **Look up before asking.** Facts are your job: read the bible and grep the
   manuscript (a sub-agent for a long manuscript) for what is already
   established. Show it as "déjà établi" with its chapter and line, and ask
   only about gaps and conflicts.
2. **Ask the frontier**, three to five questions per round, numbered, in
   the novel's language (every message to the author is in that language,
   with the form of address the author uses, tu or vous), through the agent's structured question tool when
   a question is a closed choice. An open question is marked
   `→ Question ouverte`.
3. **Write as you go.** After each round, write the settled answers into the
   file the calling skill names. A question the author defers is written
   as `{à décider}`, which settles it for this session.
4. **Challenge against canon.** An answer that contradicts the bible or the
   manuscript is called out at once, with the quote: "La fiche dit X (ch3,
   l. 12), tu viens de dire Y. Lequel ?"
5. **Recompute** the frontier from the answers and ask the next round.

## Done

The frontier is empty: every branch answered or `{à décider}`, every answer
written, nothing silently assumed. Summarise what was decided in five
lines at most and stop; the calling skill takes over.
