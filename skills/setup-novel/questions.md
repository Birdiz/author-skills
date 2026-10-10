# Questions

How `setup-novel` asks each `NOVEL.md` field. Every question shows the
detected value as the recommended answer, the definition, what the notion
is not, an example, and what the answer changes. Examples from the
manuscript are quoted with chapter and line; examples from published works
come only from this file.

Fields detected without the author (chapters, order, chapter id,
sub-agents) are shown for confirmation in one line, not asked.

## language

« Le roman est-il écrit en français ? »

Changes: the proofreading tool (Grammalecte is French only) and the
language of every question and report.

## narrative_tense

« La narration est-elle au <temps détecté> ? »

- Definition: the tense of the narration, outside dialogue: passé simple et
  imparfait, présent, passé composé.
- Not: the tenses in dialogue, or a flashback in the plus-que-parfait.
- Example: one narration sentence from the manuscript, quoted.
- Changes: `proofread` reports narration that leaves this tense, always as
  « à confirmer ».

## person, pov

« La narration est-elle à la <personne> personne, du point de vue de
<personnages> ? »

- Definition: who tells (je, il/elle) and through whose perception the
  reader sees: one character, one per chapter, or an omniscient narrator
  who knows what every character thinks.
- Not: who speaks in dialogue.
- Example: a sentence giving a point-of-view character's perception or
  thought, quoted.
- Changes: `check-continuity` records each chapter's point of view in its
  fact extracts, and tells a character's perception from the narration.

## misleading_narration

First « La narration fait-elle foi ? », then only if the answer is no,
« Quels narrateurs peuvent tromper le lecteur ? ».

- Definition: the narration (outside dialogue and reported thoughts) states
  as true something false in the story, and the reader learns it later or
  never. This happens mostly with a first-person narrator, or a
  point-of-view character whose narration is deliberately skewed.
- Not:
  - a character lying in dialogue: « — Je n'y étais pas, dit-il. »;
  - a false belief reported as a belief: « Elle ne reviendra pas,
    pensa-t-il. »;
  - a point of view that sees only part of the facts, without stating
    anything false;
  - a dream or vision marked as such.
- Published examples:
  - Agatha Christie, *Le Meurtre de Roger Ackroyd* (1926): the narrator,
    Dr Sheppard, is the murderer and hides it until the end;
  - Kazuo Ishiguro, *Les Vestiges du jour* (1989): Stevens, the butler,
    deceives himself and the reader about his loyalty to Lord Darlington
    and his feelings for Miss Kenton;
  - Gillian Flynn, *Les Apparences* (2012): Amy's diary, half the chapters
    of part one, is a fabrication meant to have Nick accused;
  - Gene Wolfe, *L'Ombre du bourreau* (1980): Severian claims to forget
    nothing, yet his account leaves out and bends what suits him.
- Borderline: free indirect style (style indirect libre), the narration
  taking on a character's thought without « pensa-t-il »: « Trop tard,
  encore une fois. Pourquoi revenait-il toujours ici ? » Fact extraction records it as that
  character's thought when the context marks it (a mirror, an exclamation,
  a question to oneself), so it never needs this setting.
- Manuscript example: a real narration sentence, quoted, with an imagined
  later contradiction (« Imagine qu'un ch6 écrive… ») to show what the
  setting changes. Never present an existing passage as a contradiction:
  that is `check-continuity`'s job, with verification.
- Changes: `check-continuity` treats a contradiction in these narrators'
  narration as possibly deliberate and asks the author instead of
  confirming it.

## dialogue_marking

« Les dialogues sont-ils marqués par <marque détectée> ? »

- Definition: how a line of dialogue starts: a dash at the start of the
  line, or quotation marks.
- Example: one dialogue line from the manuscript, quoted.
- Changes: how `proofread` and the fact extraction recognise dialogue.

## dialogue

« Les dialogues peuvent-ils s'écarter de la grammaire pour rendre l'oral ? »

- Yes (`lenient`): « J'sais pas » or « Y a personne » is the character's
  voice; `proofread` reports only clear typos in dialogue, as
  « à confirmer ».
- No (`strict`): dialogue is checked like narration.
- Example: an oral form found in the manuscript's dialogue, quoted.

## typography

One question per key, each showing both forms and their counts in the
manuscript:

- `dialogue_dash`: « — » (cadratin) or « – » (demi-cadratin);
- `quotes`: « … » or “…”;
- `space_before_high_punctuation`: espace fine insécable (U+202F, the
  Imprimerie nationale rule) or espace insécable (U+00A0) before `; : ! ?`;
- `apostrophe`: ’ (typographique) or ' (droite);
- `ellipsis`: … (one character) or ... (three dots).

« Garde-t-on <forme majoritaire> ? » Changes: `proofread` reports the other
form everywhere. `ignore` leaves the key unchecked.

## checker

« Grammalecte est-il installé, à <chemin> ? » Changes: whether `proofread`
runs a deterministic pass before its own reading.
