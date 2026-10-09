# Proofreading scope

## In scope

An error is what a French grammar reference (Grevisse, Bescherelle, the
Imprimerie nationale's typographic rules) marks wrong, whatever the
author's intent.

- **Orthographe**: lexical spelling, accents, hyphens, elisions, capitals.
  Names and invented words: the lexicon is the reference.
- **Accords**: noun and adjective, subject and verb, past participles
  (with *être*, with *avoir* and a preceding direct object, pronominal
  verbs), *tout*, *même*, *quel que*, numerals, colours.
- **Conjugaison**: wrong forms, indicative against subjunctive after a
  governing word, conditional against future.
- **Temps**: concordance in subordinate clauses; narration that leaves
  `narrative_tense` (always `à confirmer`: a shift may be deliberate);
  dialogue is not checked against `narrative_tense`.
- **Grammaire**: missing *ne*, wrong prepositions, wrong pronouns (*dont*,
  *duquel*, *leur*/*leurs*), homophones (*a*/*à*, *ces*/*ses*, *quand*/*quant*).
- **Ponctuation**: missing or doubled marks, a comma between subject and
  verb, unclosed quotes or brackets.
- **Typographie**, as `NOVEL.md` sets it: spaces before `; : ! ?` and
  inside « », dialogue dashes, apostrophes, ellipses, quotation marks.

## Dialogue

With `dialogue: lenient`, oral speech in dialogue is the character's voice:
report only typos and forms no speaker would produce, as `à confirmer`.
With `strict`, dialogue follows the narration's rules.

## Out of scope

Leave these unreported, even when tempting: they belong to the author or to
other skills.

- Style: repetition, word choice, sentence length, rhythm, clichés.
- Register, unless it is a plain error.
- Continuity of facts, names against sheets, timeline: `check-continuity`.
- Extracts listed in `.proofread/intentional.md`.
