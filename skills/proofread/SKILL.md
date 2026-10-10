---
name: proofread
description: Strictly proofread chapters of a novel (spelling, grammar, conjugation, tense consistency, punctuation, typography), report every error with its correction, and apply only the corrections the author validates. No style, no continuity.
disable-model-invocation: true
argument-hint: "[chapitres, ex. ch3 | ch3-ch7 | tout]"
---

# proofread

Version: 0.4.0 (author skills, see CHANGELOG)

Input: `NOVEL.md`, `bible/LEXICON.md` and `.proofread/intentional.md` if
they exist, the chapters named in the argument (ask if none). Output:
`.proofread/<chapter-id>.md`, then the validated corrections in the
manuscript. Refuse to run without `NOVEL.md`:
point to `/setup-novel`.

What is an error and what is out of scope: [scope](scope.md). Proofreading
never touches style: a sentence that is correct stays as it is, however it
could be improved.

## 1. Checker pass

When `checker` is `grammalecte`, per chapter:

1. Write a plain-text copy in a temporary directory with the same lines:
   strip heading `#` marks and emphasis markers (`*`, `_`), keep every line,
   so line numbers match the chapter.
2. Run `<checker_command> -f <copy> -j`, with `-off` for every typography
   option that `NOVEL.md` sets to `ignore` or to a form the checker treats
   as an error (an ordinary space before `; : ! ?` against its
   non-breaking-space rule): `<checker_command> -lo` lists the options. Paragraph indexes in the JSON map to lines of the copy:
   check on the first error that the span quotes the right words.
3. Drop spelling errors on terms and variants in the lexicon.

When `checker` is `none`, skip to step 2 and say in the report that no
checker ran.

## 2. Reading pass

Read the whole chapter, a sub-agent per chapter when there are several and
`sub_agents: yes`. Every rule in [scope](scope.md) is applied to every
line, including what the checker missed: agreements across long sentences,
past participles, agreements with invented words from their gender in the
lexicon, tense against `narrative_tense`, typography against `NOVEL.md`.
Review each checker error too: a false positive is dropped with no entry.

## 3. Report

Write `.proofread/<chapter-id>.md`, replacing the previous report:

```markdown
# Relecture ch3 — 2026-10-09
Checker : grammalecte | aucun

| ID | Ligne | Extrait | Correction | Règle | Certitude |
|---|---|---|---|---|---|
| P3-001 | 12 | « les lettres qu'il avait écrit » | « les lettres qu'il avait écrites » | accord du participe passé avec avoir, COD avant | certaine |
| P3-002 | 40 | « Elle entre dans la salle » | « Elle entra dans la salle » | temps de narration : passé simple | à confirmer |
| P3-003 | tout le chapitre | 196 × « ' » | « ’ » | apostrophe typographique (`NOVEL.md`) | certaine |
```

- **Extrait**: verbatim, long enough to be unique on its line.
- **Correction**: the same extract with only the error's span changed.
- **Typography**: a form `NOVEL.md` rules out everywhere (apostrophes,
  spaces, ellipses, dashes) is one row per rule for the chapter, with its
  count, applied to every occurrence.
- **Certitude**: `certaine` when a grammar reference marks it wrong
  whatever the intent; `à confirmer` when it could be deliberate (tense
  shift, oral speech, rare spelling, unusual typography). It describes the
  error, never the author's answer: validation does not change it.

Show the author, in the novel's language and with the form of address
they use (tu or vous), the counts per chapter and certainty, and the `à
confirmer` rows in full.

## 4. Validation

Apply nothing before the author validates. Offer exactly these answers,
with the number of rows each covers:

- `tout`: every row, `à confirmer` included;
- `les certaines`: only the rows marked `certaine`;
- ids (`P3-001, P3-004`) or ranges (`P3-001..P3-009`);
- `tout sauf P3-007`.

Only these forms validate a row. A question, a remark or a wish is
answered, then the choice is offered again with the rows still open. A refused row the author calls deliberate goes into
`.proofread/intentional.md` (chapter id, extract, reason), which every
later run reads: an extract listed there is not reported again.

## 5. Apply

Before applying, say in one line which rows will be applied and which stay
open. For each validated id, replace the extract with the correction on its
line, nothing else; a typography row replaces every occurrence of its form
in the chapter. If the extract is no longer on that line exactly once, skip
it and say so. Then re-run step 1 on the changed chapters and report any
new checker error the corrections introduced. Mark applied rows
`appliqué` in the report.

## Done

Every row of every requested chapter is applied, refused by the author, or
skipped with its reason; the author is told to review with `git diff`.
