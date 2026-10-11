---
name: validated-corrections
description: Protocol for changing a novel's manuscript only with the author's validation (report rows with ids and certainty, the exact answers that validate, applying only the validated rows, remembering deliberate forms). Use whenever a skill proposes changes to manuscript files.
---

# validated-corrections

Version: 0.7.2 (author skills, see CHANGELOG)

The manuscript changes only by correction the author validated by id. The
calling skill names its report file, its id prefix and what a correction
does (replace words, insert or remove a scene break); this skill holds
the rest.

## Scope

A skill proposes rows only for what it owns: `proofread` the language,
`scene-breaks` the markers, `echoes` repetitions and tics,
`check-continuity` the canon. Anything else
noticed on the way goes into a `## Hors périmètre` section of the report,
one line each (line, quote, what was noticed, the skill that owns it),
with no correction and no row: the owning skill has the checks this one
skipped (for continuity, the extraction, the independent verification and
the choice between text, sheet and ruling).

## Rows

Every proposed change is one row: id, line, extract, correction, reason,
certainty.

- **Extract**: verbatim, long enough to occur once on its line.
- **Correction**: the same extract with only the change made, or, where
  the calling skill allows a reformulation, the smallest rewording of the
  clause that fixes it. Two changes
  close enough to share words are one row, so no row invalidates another.
- **Certainty**: `certaine` when a reference rule settles it whatever the
  intent; `à confirmer` when it could be deliberate. It describes the
  change, never the author's answer.
- A change applied to the whole chapter (a typographic form) is one row
  with its count.
- A row may offer numbered alternatives, separated by `|`, when the
  calling skill allows it. Each is the whole extract as it will be
  applied.

## Presenting

In the novel's language, with the author's form of address (tu or vous):
the counts per certainty first. Then the rows, through the form when the
agent has a multiple-choice question tool, typed answers otherwise.

### Form

The author clicks instead of typing ids, so a report of thirty rows does
not cost thirty typed answers.

1. When there are `certaine` rows, one question first: `Appliquer les N
   certaines` or `Les passer en revue` (they then go through the form with
   the others).
2. The other rows four per call, one question per row: the id as header,
   the line, the extract and the reason as question. Options:
   - a row with alternatives: its alternatives (three at most), each in
     full, then `Garder (voulu)`;
   - a row without: `Appliquer`, with the correction in full, then
     `Garder (voulu)`.

   The free-text answer is the author's own word, under the rule below,
   or a remark, answered before the row is asked again. An own word that
   needs another change comes back as its own question: `Appliquer` with
   the version in full, or `Revoir les alternatives`.
3. Then the typed answers, below, for any row still open.

A click validates or refuses its row like the typed answers do;
`Garder (voulu)` is a refusal as deliberate.

### Typed answers

Every `à confirmer` row in full, then exactly these answers, each with the
number of rows it covers:

- `tout`: every row;
- `les certaines`: only the `certaine` rows;
- ids (`P3-001, P3-004`) or ranges (`P3-001..P3-009`);
- `tout sauf P3-007`;
- for a row with alternatives, its id with a number or the author's own
  word (`E4-001 : 2`, `E4-003 : la veilleuse`), several separated by
  commas.

Offer only the answers that cover at least one row. A row with
alternatives is validated only by the last form: `tout`, `les certaines`,
an id or a range alone leave it open. The author's own word is applied as
given when no other word of the extract has to change; when it needs
another change (an agreement: « le fanal voisin » becomes « la veilleuse
voisine »), it is added to the row as the next alternative, shown in full,
and the row stays open until the author names it.

Only these forms and the form's options validate a row. A question, a
remark or a wish is answered, then the choice is offered again with the
rows still open.

A row the author refuses as deliberate goes into the calling skill's
`intentional.md` (chapter id, extract, reason). Every later run reads it
and does not propose that extract again.

## Applying

1. Say in one line which rows will be applied and which stay open.
2. Apply each validated row on its line, nothing else, from the last line
   of the chapter to the first: a row that adds or removes lines (a split
   paragraph, a scene break) then leaves the line numbers of the rows still
   to apply intact. A row whose extract no longer occurs exactly once on
   its line is skipped, and said so. Whole-chapter rows are applied last.
3. Mark applied rows `appliqué` in the report.
4. Tell the author to review with `git diff`.

## Done

Every row is applied, refused, skipped with its reason, or still open and
listed as such to the author.
