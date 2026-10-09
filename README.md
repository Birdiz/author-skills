# author-skills

Agent skills for writing a novel: strict proofreading, character and world
building, continuity checks against a story bible, brainstorming, and a muse
that never writes for you.

Small, composable, and readable by any coding agent. The structure follows
[mattpocock/skills](https://github.com/mattpocock/skills): user-invoked
skills orchestrate, model-invoked skills hold the discipline, and a shared
vocabulary ([CONTEXT.md](CONTEXT.md)) keeps them speaking the same language.

## Status

Early. Every skill is written as a first version; none has run on a real
manuscript yet. Grammalecte's command line is used through the flags its
documentation lists, confirmed by `setup-novel` on the author's machine.

## Install

**Claude Code: as a plugin.** Skills are namespaced `author-skills:<name>`.

```
/plugin marketplace add Birdiz/author-skills
/plugin install author-skills@birdiz-author
```

**Other agents, or to edit the skills:** copy the folders under `skills/`
into the agent's skills directory.

## The novel project

The skills work in the novel's own repository, never in this one:

```
<novel>/
├── NOVEL.md                 # setup-novel
├── manuscript/              # one Markdown file per chapter, one paragraph per line
│   ├── 01-<titre>.md
│   └── ...
├── bible/                   # story-bible
│   ├── LEXICON.md
│   ├── characters/
│   ├── world/places/
│   ├── world/systems/
│   ├── timeline.md
│   └── rulings.md
├── .continuity/             # check-continuity: facts cache, findings
├── .proofread/              # proofread: reports, deliberate deviations
└── notes/                   # brainstorm briefs, muse sparks
```

## Flow

1. `/setup-novel`, once: layout, language, tense, point of view,
   typography, Grammalecte.
2. `/build-character` and `/build-world` as the story needs them.
3. Write.
4. `/proofread <chapitres>`: report, then validated corrections.
5. `/check-continuity [axes] [chapitres]`: extract, compare, verify,
   arbitrate.
6. When stuck: `/brainstorm <idée>` if an idea will not take shape,
   `/muse` if there is no idea.

## Skills

**User-invoked** (they orchestrate)

- [setup-novel](skills/setup-novel/SKILL.md): configure the novel project
  once.
- [proofread](skills/proofread/SKILL.md): strict proofreading (spelling,
  grammar, conjugation, tenses, punctuation, typography), Grammalecte then
  a full reading; applies only validated corrections.
- [build-character](skills/build-character/SKILL.md): a core interview,
  then physique, psychology, savoir, savoir-faire, savoir-être, voice,
  relations, arc.
- [build-world](skills/build-world/SKILL.md): places from building to
  world, and systems (magic, factions, religions...), with optional
  deepening.
- [check-continuity](skills/check-continuity/SKILL.md): characters,
  situations and world axes, verified from a fresh context, arbitrated by
  the author.
- [brainstorm](skills/brainstorm/SKILL.md): frame a fuzzy idea into a
  brief.
- [muse](skills/muse/SKILL.md): sparks from the author's own story when
  the page stays blank.

**Model-invoked** (they hold the discipline)

- [story-bible](skills/story-bible/SKILL.md): bible layout, sheet
  templates, lexicon, timeline, rulings, annotations, the canon rule.
- [grilling](skills/grilling/SKILL.md): the interview in rounds, in ask or
  suggest mode.
- [continuity-findings](skills/continuity-findings/SKILL.md): the format of
  a contradiction.

A user-invoked skill may rely on model-invoked ones, never on another
user-invoked one.

## Decisions

- [0001](docs/adr/0001-files-are-the-contract.md): files are the contract
  between skills.
- [0002](docs/adr/0002-the-author-rules-on-canon.md): the author rules on
  canon.
- [0003](docs/adr/0003-invariants.md): invariants are not configurable
  (no prose, validated corrections only, no style in proofreading, quotes
  in every finding).

## Language

Skills are written in English. Templates, questions and everything the
author reads are in French, the language of the novels this set was written
for; skills translate the templates when `NOVEL.md` declares another
language.

## License

MIT.
