---
name: validated-corrections
description: Protocol for changing a novel's manuscript only with the author's validation (report rows with ids and certainty, the exact answers that validate, applying only the validated rows, remembering deliberate forms). Use whenever a skill proposes changes to manuscript files.
---

# validated-corrections

Version: 0.5.0 (author skills, see CHANGELOG)

The manuscript changes only by correction the author validated by id. The
calling skill names its report file, its id prefix and what a correction
does (replace words, insert or remove a scene break); this skill holds
the rest.

## Rows

Every proposed change is one row: id, line, extract, correction, reason,
certainty.

- **Extract**: verbatim, long enough to occur once on its line.
- **Correction**: the same extract with only the change made. Two changes
  close enough to share words are one row, so no row invalidates another.
- **Certainty**: `certaine` when a reference rule settles it whatever the
  intent; `à confirmer` when it could be deliberate. It describes the
  change, never the author's answer.
- A change applied to the whole chapter (a typographic form) is one row
  with its count.

## Presenting

In the novel's language, with the author's form of address (tu or vous):
the counts per certainty, then every `à confirmer` row in full. Then offer
exactly these answers, each with the number of rows it covers:

- `tout`: every row;
- `les certaines`: only the `certaine` rows;
- ids (`P3-001, P3-004`) or ranges (`P3-001..P3-009`);
- `tout sauf P3-007`.

Only these forms validate a row. A question, a remark or a wish is
answered, then the choice is offered again with the rows still open.

A row the author refuses as deliberate goes into the calling skill's
`intentional.md` (chapter id, extract, reason). Every later run reads it
and does not propose that extract again.

## Applying

1. Say in one line which rows will be applied and which stay open.
2. Apply each validated row on its line, nothing else. A row whose extract
   no longer occurs exactly once on its line is skipped, and said so.
   Whole-chapter rows are applied last.
3. Mark applied rows `appliqué` in the report.
4. Tell the author to review with `git diff`.

## Done

Every row is applied, refused, skipped with its reason, or still open and
listed as such to the author.
