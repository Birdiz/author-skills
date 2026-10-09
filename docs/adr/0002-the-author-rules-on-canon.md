# 0002: The author rules on canon

Status: accepted, 2026-10-09

## Context

When a sheet and the text disagree, three policies exist: the bible wins (the
text is corrected), the text wins (the bible is a cache of the text), or the
author decides each time. Fiction also contains deliberate contradictions:
lies, beliefs, unreliable narrators, characters who change.

## Decision

No skill resolves a conflict of canon on its own. `check-continuity` raises
it with both quotes, proposes a resolution, and applies only what the author
chooses: update the sheet, apply a correction to the text, or record a
ruling that it is intentional.

Rulings live in `bible/rulings.md` and are read by every later check, so a
conflict ruled intentional is never raised again.

## Consequences

- Checks are slower to close than with an automatic policy, and the author
  keeps the canon.
- The bible can follow a novel written by discovery as well as by plan.
- A finding has two independent fields: `status` (is it a real
  contradiction?) and `resolution` (what the author did about it).
