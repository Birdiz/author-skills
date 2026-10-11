---
name: proofread
description: Strictly proofread chapters of a novel (spelling, grammar, conjugation, tense consistency, punctuation, typography), report every error with its correction, and apply only the corrections the author validates. No style, no continuity.
disable-model-invocation: true
argument-hint: "[chapitres, ex. ch3 | ch3-ch7 | tout]"
---

# proofread

Version: 0.6.1 (author skills, see CHANGELOG)

Input: `NOVEL.md`, `bible/LEXICON.md` and `.proofread/intentional.md` if
they exist, the chapters named in the argument (ask if none). Output:
`.proofread/<chapter-id>.md`, then the validated corrections, per
`validated-corrections`. Refuse to run without `NOVEL.md`: point to
`/setup-novel`.

What is an error and what is out of scope: [scope](scope.md). Proofreading
never touches style: a sentence that is correct stays as it is, however it
could be improved.

The bar is **every error in the chapter**. One reading of a whole chapter
misses errors, so the work is split: tools first, then short batches read
twice, each time for one family of rules.

## 1. Checker

When `checker` is `grammalecte`, per chapter:

1. Write a plain-text copy in a temporary directory with the same lines:
   strip heading `#` marks and emphasis markers (`*`, `_`), keep every
   line, so line numbers match the chapter.
2. Run `<checker_command> -f <copy> -j`, with `-off` for every typography
   option (typography is step 2's) and for options `NOVEL.md` contradicts;
   `<checker_command> -lo` lists them. Paragraph indexes in the JSON map
   to lines of the copy: check on the first error that the span quotes the
   right words.
3. Drop spelling errors on terms and variants in the lexicon.

When `checker` is `none`, say in the report that no checker ran.

## 2. Typography

Run [the typography script](scripts/typography.py) on the chapter:

```
python3 scripts/typography.py <chapter> --apostrophe ’ --ellipsis … \
  --space-before-high nnbsp|nbsp|space --quotes «» \
  --quote-space nnbsp|nbsp|space --dialogue-dash — --scene-break "* * *"
```

The path is relative to this skill's directory. Map each `NOVEL.md`
typography key to its option (`ignore` where the author chose it; an
ordinary space is `space`, U+00A0 `nbsp`, U+202F `nnbsp`). Its rows are
`certaine`, except dialogue lines when `dialogue: lenient`.

## 3. Reading

Cut the chapter into batches of about fifteen paragraphs, at a scene break
when one falls nearby. Each batch is read **twice**, once per family of
[scope](scope.md): **A, langue** and **B, ponctuation et dialogue**.

Each reading is a fresh sub-agent when `sub_agents: yes`, given only: the
batch's lines with their numbers, the paragraph before it for context,
`NOVEL.md`, the lexicon, `intentional.md`, and its family from scope. It
reads sentence by sentence, applies every rule of its family to every
sentence, and returns its rows and the lines it covered (`couvert : l. 41
à 69`). A batch whose coverage falls short is read again. Without
sub-agents, read the batches and families one at a time in this session.

## 4. Report

Merge the rows of steps 1 to 3: one row per extract (rows sharing words
merge), checker false positives dropped. Write `.proofread/<chapter-id>.md`,
replacing the previous report:

```markdown
# Relecture ch3 — 2026-10-09
Checker : grammalecte | aucun
Lecture : 5 lots × 2 familles, couverture complète

| ID | Ligne | Extrait | Correction | Règle | Source | Certitude |
|---|---|---|---|---|---|---|
| P3-001 | 12 | « les lettres qu'il avait écrit » | « les lettres qu'il avait écrites » | accord du participe passé avec avoir, COD avant | lecture A | certaine |
| P3-002 | 40 | « Elle entre dans la salle » | « Elle entra dans la salle » | temps de narration : passé simple | lecture A | à confirmer |
| P3-003 | 58 | « J'arrive. Elle posa » | « J'arrive. ¶ Elle posa » | narration collée à une réplique | lecture B | à confirmer |
| P3-004 | 71 | « En ouvrant la porte, le vent s'engouffra » | « Quand il ouvrit la porte, le vent s'engouffra » | reformulation : participe détaché dont le sujet implicite n'est pas celui de la phrase | lecture A | à confirmer |
| P3-005 | tout le chapitre | 196 × « ' » | « ’ » | apostrophe (`NOVEL.md`) | typographie | certaine |
```

**Source**: `grammalecte`, `typographie`, `lecture A` or `lecture B`; it
shows which step finds what, and which one missed an error found later.
A `¶` in a correction is a paragraph break: the line is split in two, with
a blank line between.

A construction error that no word replacement fixes gets the smallest
rewording of its clause: `à confirmer`, and its **Règle** starts with
`reformulation :`. Keep the author's words and order wherever the fix
allows.

## 5. Validate and apply

Per `validated-corrections`, with ids `P<N>-<NNN>` and
`.proofread/intentional.md`. Then re-run steps 1 and 2 on the changed
chapters and report any new error the corrections introduced.

## Done

Every batch covered by both families; every row applied, refused, skipped
with its reason, or listed as open.
