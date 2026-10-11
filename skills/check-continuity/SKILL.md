---
name: check-continuity
description: Check a novel's continuity on three axes (characters, situations, world) against itself and its bible, verify each contradiction from a fresh context, then have the author arbitrate each one. Reports with quotes; changes nothing without the author.
disable-model-invocation: true
argument-hint: "[characters|situations|world ...] [chapitres]"
---

# check-continuity

Version: 0.7.0 (author skills, see CHANGELOG)

Input: `NOVEL.md`, the manuscript, the bible. Output: `.continuity/facts/`,
`.continuity/findings/<axis>.md` per `continuity-findings`, and what the
author chooses at arbitration. Refuse to run without `NOVEL.md`: point to
`/setup-novel`.

Arguments: the axes (default all three) and the chapters (default all).
Chapters narrow what is reported, not what is read: every chapter's facts
are extracted and compared, since a contradiction can span the whole
novel, and only findings with a location in the named chapters are kept.

**Resume**: when a findings file holds `unverified` findings from an earlier
run, start at step 3 for those, then ask the author whether to run a new
check.

## 1. Extract

For each chapter, compute `git hash-object <file>` (or `sha256sum` outside
git). A facts file whose `hash` matches is reused. Otherwise extract the
chapter's facts per [extraction](extraction.md) into
`.continuity/facts/<chapter-id>.md`: one sub-agent per chapter when
`sub_agents: yes`, given only file paths.

Extraction records what the text states and who states it. It does not
judge.

## 2. Compare

One sub-agent per requested axis, in parallel when possible, given only
file paths: `NOVEL.md`, the facts files, the bible, its axis section of
[axes](axes.md), `continuity-findings`, and the existing findings file of
its axis. It compares facts with facts and facts with the bible, and
appends findings as `unverified`. Without sub-agents, run the axes one
after the other.

## 3. Verify

Verification is done by a context that wrote no finding: a sub-agent per
axis given file paths only (findings file, chapters, bible, `NOVEL.md`).
Without sub-agents, stop here and tell the author to run
`/check-continuity` again in a new session, which resumes at this step for
every `unverified` finding.

Per finding, try to show it is not a contradiction:

1. **Re-read** each location with its surrounding paragraphs. A misread
   quote refutes the finding.
2. **Who says it**: a lie, a rumour, a belief, a dream, a character's
   error, free indirect style voicing a character, a narrator listed in
   `misleading_narration`. A statement that is
   only a character's word does not contradict a fact; it may still be a
   `knowledge` finding.
3. **What happens in between**: time passing, healing, magic, a disguise,
   an explanation in another chapter.
4. **Rulings**: a ruling in `bible/rulings.md` whose scope covers it.
5. **Annotations**: `{dès}`, `{jusqu'à}`, `{croyance}`, `{à confirmer}`.

Set `status: confirmed` or `refuted`, correct the impact if wrong, and fill
**Possible intent** with what was found.

## 4. Arbitrate

Present the confirmed findings whose resolution is `open` or `deferred`,
`major` first, three to five per round
through `grilling` in **suggest** mode: each with both quotes and the
**Resolutions** options, the recommended one first.

Apply exactly the author's choice, and set `resolution`:

- **bible-updated**: edit the sheet per `story-bible`.
- **text-corrected**: propose the exact replacement (only the conflicting
  words) and apply it per `validated-corrections`, with ids `T<N>-<NNN>`.
- **ruled**: append a ruling to `bible/rulings.md` with its scope.
- **deferred**: leave it; the next run presents it again.

## Done

Every confirmed finding presented is resolved or deferred by the author.
Report per axis: new, confirmed, refuted, resolved, deferred, and the
chapters whose facts were re-extracted.
