# 0003: Invariants are not configurable

Status: accepted, 2026-10-09

## Context

`setup-novel` absorbs what varies between novels. Some rules protect the
author's voice and the reliability of the checks, and have only one
legitimate answer.

## Decision

A question belongs in `NOVEL.md` only if two legitimate answers exist and a
named skill reads it. The following have one, and are written into the
skills with their reason:

1. **The agent never writes prose.** The voice is the author's. `muse` gives
   sparks, `brainstorm` gives beats and briefs, `build-character` and
   `build-world` ask rather than invent.
2. **The manuscript changes only by validated correction.** The agent
   proposes the exact replacement, the author validates it by id, and only
   the error's span is replaced: no rewording, no reordering. Adding or
   removing a scene-break marker, or splitting a paragraph, is a correction
   too. `validated-corrections` holds the protocol.
3. **Proofreading never touches style.** Repetition, word choice, rhythm and
   continuity are out of scope; a deliberate deviation (oral speech, a
   tense shift) is reported as uncertain, never as certain.
4. **Every finding quotes the text.** A contradiction without its line and
   quote cannot be checked by the author.
5. **The author rules on canon.** See ADR 0002.

## Consequences

- No `NOVEL.md` field disables these.
- Anyone forking the set can change them, and can see what they give up.
