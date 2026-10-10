# Proofreading scope

An error is what a French grammar reference (Grevisse, Bescherelle, the
Imprimerie nationale's typographic rules) marks wrong, whatever the
author's intent. Each reading applies one family to every sentence.

## Family A: langue

- **Orthographe**: lexical spelling, accents, hyphens, elisions, capitals.
  Names and invented words: the lexicon is the reference.
- **Accords**: noun and adjective, subject and verb (including an inverted
  or distant subject), past participles (with *être*, with *avoir* and a
  preceding direct object, pronominal verbs), *tout*, *même*, *quel que*,
  numerals, colours, agreement with an invented word from its gender in
  the lexicon.
- **Conjugaison**: wrong forms (« il cousa », « elle résolva »), indicative against
  subjunctive after a governing word, conditional against future.
- **Temps**: concordance in subordinate clauses; narration that leaves
  `narrative_tense` (always `à confirmer`); dialogue is not checked against
  `narrative_tense`.
- **Constructions**: a sentence without a finite verb that is not a
  deliberate nominal sentence; a detached participle or adjective whose
  implied subject is not the sentence's subject (« En ouvrant la porte, le
  vent s'engouffra »); a conditional after a hypothetical *si*
  (after a *si* of opposition, `à confirmer`); a missing word.
- **Grammaire**: missing *ne*, wrong prepositions, wrong pronouns (*dont*,
  *duquel*, *leur*/*leurs*), homophones (*a*/*à*, *ces*/*ses*, *dont*/*donc*,
  *quand*/*quant*, *ou*/*où*, infinitive against past participle).

## Family B: ponctuation et dialogue

- **Ponctuation**: missing or doubled marks, a comma between subject and
  verb, a missing comma around a vocative (« Bonjour, Paul »), unclosed
  quotes or brackets, a sentence without its final mark.
- **Dialogue**: a narration sentence glued to a reply without an incise
  (« — J'arrive. Elle posa son verre. »), corrected
  by a paragraph break, `à confirmer`; an incise without its comma or with
  a capital (« dit-il », not « Dit-il »); a change of speaker without a
  new dash; a reply whose dash is missing.
- **Typographie** that the script cannot see: quotation marks that open
  and never close, a dash used as a hyphen inside a word.

## Dialogue

With `dialogue: lenient`, oral speech in dialogue is the character's voice:
report only typos and forms no speaker would produce, as `à confirmer`.
With `strict`, dialogue follows the narration's rules. Family B applies to
dialogue in both cases.

## Out of scope

Leave these unreported, even when tempting: they belong to the author or to
other skills.

- Style: repetition, word choice, sentence length, rhythm, clichés.
- Register, unless it is a plain error.
- Continuity of facts, names against sheets, forms of address, timeline:
  `check-continuity`.
- Scene breaks: `scene-breaks`.
- Extracts listed in `.proofread/intentional.md`.
