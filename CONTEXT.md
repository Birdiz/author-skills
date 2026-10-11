# Context

Shared vocabulary for these skills. Use these terms as defined, in skills,
bible files, findings and reports.

- **Author**: the person writing the novel. Owns every creative decision and
  every ruling on canon.
- **Novel project**: the repository holding one novel: `NOVEL.md`, the
  manuscript, the bible, and the generated files. Never this repository.
- **Novel config**: `NOVEL.md` at the root of the novel project, written by
  `setup-novel`. Every other skill refuses to run without it.
- **Manuscript**: the novel's text, one Markdown file per chapter, one
  paragraph per line.
- **Chapter id**: `ch<N>`, from the leading number of the chapter's file name.
- **Bible**: the author's canon outside the text: sheets, lexicon, timeline,
  rulings. Format owned by `story-bible`.
- **Sheet**: one bible file for one character, place or system.
- **Place**: a sheet for a location at one **scale** (building, district,
  village, city, region, country, continent, world), linked to its parent.
- **System**: a sheet for a rule-bearing part of the world that is not a
  location: magic, faction, religion, technology, species, language,
  calendar, economy, past event.
- **Lexicon**: the spelling, gender and variants of every proper noun and
  invented word. Read by `proofread` so invented words are not errors.
- **Annotation**: a marker on a sheet fact giving its validity in time or its
  reveal status (`{dès ch12}`, `{secret}`, `{révélé ch20}`...).
- **Canon**: what is true in the story: the bible, the manuscript, and the
  rulings between them. When the bible and the text disagree, neither wins:
  the author rules.
- **Ruling**: the author's recorded decision on a conflict of canon,
  including "intentional". Rulings stop the same conflict being raised twice.
- **Fact extract**: the facts one chapter states, with line and quote,
  written by `check-continuity` and reused until the chapter changes.
- **Axis**: one dimension of a continuity check: characters, situations,
  world. One axis, one findings file.
- **Finding**: a contradiction found by an axis, in the `continuity-findings`
  format, with its quotes.
- **Verification**: an attempt, from a context that did not write the finding,
  to show it is not a contradiction (a lie, a belief, time passing, a
  ruling).
- **Arbitration**: the author choosing, per finding, which side of canon is
  right.
- **Correction**: the smallest change to the manuscript that fixes a
  validated error: replaced words, a split paragraph, a scene-break marker
  added or removed. The only change an agent makes to the manuscript, per
  `validated-corrections`.
- **Echo**: one word family repeated close enough for a reader to feel it,
  found by `echoes`. A **concentration** is the same over a passage.
- **Tic**: a word or gesture the author reaches for across a chapter or the
  novel (regarder, s'arrêter, faire).
- **Motif**: a family the author repeats on purpose, listed under
  `## Motifs` in `.echoes/intentional.md`, never reported as an echo.
- **Out-of-scope note**: something a skill noticed outside what it owns,
  listed in its report for the owning skill, never proposed as a
  correction.
- **Scene break**: the marker line (`scene_break` in `NOVEL.md`) between
  two scenes, where time, place, point of view or thread breaks.
- **Prose**: sentences that could appear in the novel. Only the author writes
  them.
- **Spark**: one line from `muse` that starts the author's thinking: a
  question, a constraint, a "what if". Never prose.
- **Idea brief**: the framed result of `brainstorm`, in `notes/ideas/`.
- **Frontier**: in an interview, the questions whose prerequisites are
  already answered. See `grilling`.
