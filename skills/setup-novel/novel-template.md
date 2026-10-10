# NOVEL.md template

Each section names the skills that read it. Values below are examples.

```markdown
# <Titre du roman>
version: 1
updated: <YYYY-MM-DD>

## Manuscript
<!-- read by: every skill -->
language: fr
chapters: manuscript/*.md
chapter_id: leading number of the file name → ch<N>
order: file name
scene_break: "* * *"
sub_agents: yes

## Narration
<!-- read by: proofread, check-continuity -->
narrative_tense: passé simple et imparfait
person: 3rd
pov: multiple, one per chapter
misleading_narration: []
dialogue_marking: tiret cadratin en début de ligne

## Proofreading
<!-- read by: proofread -->
checker: grammalecte
checker_command: python3 ~/tools/grammalecte/grammalecte-cli.py
dialogue: lenient
typography:
  dialogue_dash: "—"
  quotes: "« » avec espace fine insécable"
  space_before_high_punctuation: "U+202F"
  apostrophe: "’"
  ellipsis: "…"

## Bible
<!-- read by: story-bible, build-character, build-world, check-continuity, brainstorm, muse -->
path: bible/
```

## Fields

- `dialogue`: `lenient` reports errors inside dialogue only when they cannot
  be deliberate oral speech (a typo, not « j'sais pas »), and always as
  uncertain; `strict` checks dialogue like narration.
- `typography`: each key may be `ignore`, in which case `proofread` does
  not check it.
- `misleading_narration`: the narrators whose narration may mislead the
  reader (point-of-view characters, or `narrateur` for an external
  narrator); `[]` when the narration is always true in the story.
  `check-continuity` verification reads it. See
  [questions](questions.md) for how it is asked.
- `scene_break`: the line that marks a scene break; `scene-breaks`,
  `proofread` and `check-continuity` read it.
- `sub_agents`: whether the agent can dispatch sub-agents; skills take the
  sequential path when `no`.
