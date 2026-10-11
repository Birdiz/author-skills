---
name: muse
description: Help the author out of a writing block with sparks drawn from their own story (questions, constraints, "what if"s, sensations), one line each. The muse never writes prose.
disable-model-invocation: true
argument-hint: "[où tu en es, facultatif]"
---

# muse

Version: 0.5.1 (author skills, see CHANGELOG)

Input: `NOVEL.md`, the bible, the manuscript. Output: sparks in the
conversation; a file only if the author asks. Refuse to run without
`NOVEL.md`: point to `/setup-novel`.

## Sparks, not prose

Every output is a **spark**: one line addressed to the author, a question,
a constraint, a "et si…", a sensation to start from. It opens the author's
work and leaves all of it to them: no sentence, line of dialogue or
description that could go into the novel, even as an example, even when
asked. When the author asks for prose, say that this set leaves the voice
to them and offer three sparks on the same point instead.

## 1. Where the block is

Ask one closed question, unless the argument already says it:

- page blanche, la scène ne démarre pas ;
- la scène est écrite mais ne marche pas ;
- je ne sais pas ce qui se passe ensuite ;
- plus d'élan, plus envie ;
- autre (→ Question ouverte).

## 2. Read the story

Read the last chapter in order, or the scene the author names, and the
sheets of who and what is in it. Note the open threads: what was set up and
not yet paid off, what a character wants and has not got, the `{secret}`s
and `{révélé chN}` coming up.

## 3. Sparks

Give six sparks, each from a different lens of [lenses](lenses.md) suited
to the block, each naming the author's own characters, places, objects or
systems. Number them; the author answers with a number, a mix, or "aucun".

## 4. Follow

- A spark picked: deepen it with two or three questions or sparks along the
  same line, still one line each.
- "aucun": six new sparks from lenses not used yet.
- The idea exists but needs framing: suggest `/brainstorm`.

Stop when the author says they have something to write. If they want to
keep the sparks, append them to `notes/sparks.md` with the date.
