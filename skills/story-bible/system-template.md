# System template

The sheet written in `bible/world/systems/<slug>.md`, then the question bank
`build-world` draws from. Questions in French; translate them when
`NOVEL.md` declares another language.

Types: `magie`, `faction`, `religion`, `technologie`, `espèce`, `langue`,
`calendrier`, `économie`, `événement passé`.

A system is checkable through its **limits**: what it costs, what it cannot
do, who cannot use it. A power without a limit cannot contradict anything,
so `build-world` pushes for limits before anything else.

## Sheet

```markdown
# <Nom>

- Type : <...>
- Rôle dans l'histoire : <...>
- Chapitres : ch<N>, ...

## Ce que c'est
## Règles
- <ce que le système permet>
## Coûts et limites
- <ce qu'il coûte, ce qu'il ne peut pas faire>
## Accès
## Manifestations
## Croyances
- <ce que les gens croient> {croyance: <qui>}
## Exceptions
## Histoire
```

## Core

1. Qu'est-ce que c'est, en une phrase ?
2. Quel rôle joue-t-il dans l'histoire ?
3. Que permet-il, précisément ?
4. Que coûte-t-il à celui qui l'utilise ou y appartient ?
5. Que ne peut-il pas faire, jamais ?
6. Qui y a accès, et qui en est exclu ?
7. Comment se manifeste-t-il : ce qu'on voit, entend, ressent ?
8. Que croient les gens à son sujet qui est faux ou incomplet ?

## By type

### Magie, technologie
- Source de la puissance ? Apprentissage, durée, échecs possibles ?
- Ce qui l'amplifie, ce qui la bloque ?
- Conséquences sociales : qui en profite, qui la craint, quelles lois ?

### Faction, religion
- Objectif, hiérarchie, rites d'entrée, signes de reconnaissance ?
- Alliés, ennemis, schismes ?
- Ce qu'elle cache, à qui ?

### Espèce, peuple
- Biologie : durée de vie, sens, besoins, faiblesses ?
- Culture, langue, rapports aux autres peuples ?

### Langue
- Qui la parle ? Sonorités, règles d'écriture des noms propres ?
- Mots employés dans le texte : sens, genre, pluriel (vers le lexique) ?

### Calendrier
- Durée du jour, des mois, de l'année ? Noms des jours, mois, saisons ?
- Ère et an zéro ? Fêtes ? Date de début du roman ?

### Économie
- Monnaie, unités, prix courants (un repas, un cheval, une nuit
  d'auberge) ?

### Événement passé
- Date, lieu, acteurs ? Ce qui s'est vraiment passé, et ce qu'on en raconte ?
