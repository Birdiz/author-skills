# Place template

The sheet written in `bible/world/places/<slug>.md`, then the question bank
`build-world` draws from: a common core for every scale, then the questions
of the place's own scale. Questions in French; translate them when
`NOVEL.md` declares another language.

Scales, from smallest: `bâtiment`, `quartier`, `village`, `ville`, `région`,
`pays`, `continent`, `monde`.

## Sheet

```markdown
# <Nom>

- Échelle : <bâtiment | quartier | village | ville | région | pays | continent | monde>
- Contenu dans : [<parent>](<slug-parent>.md)
- Gentilé, variantes du nom : <...>
- Rôle dans l'histoire : <...>
- Chapitres : ch<N>, ...

## Impression
## Aspect et sens
## Habitants
## Pouvoir
## <Sections de l'échelle>

## Distances et trajets

| Vers | Distance | À pied | À cheval | Autre |
|---|---|---|---|---|

## Approfondissement
```

The distances table matters: `check-continuity` uses it to test travel
times.

## Common core

1. Comment s'appelle ce lieu, et comment l'appellent ceux qui y vivent ?
   Quel est le gentilé ?
2. Dans quel lieu plus vaste se trouve-t-il ?
3. Quel rôle joue-t-il dans l'histoire, et dans quels chapitres ?
4. Quelle impression doit-il laisser au lecteur ?
5. À quoi ressemble-t-il ? Qu'y entend-on, qu'y sent-on ?
6. Qui y vit, et combien ?
7. Qui y détient le pouvoir ?
8. À quelle distance, et à combien de temps, des autres lieux de l'histoire ?

## By scale

### Bâtiment
- Fonction, propriétaire, état ?
- Plan : étages, pièces, accès, issues, cachettes ?
- Matériaux, lumière, chaleur ?

### Quartier, village
- Places, rues, bâtiments notables ?
- Institutions : temple, auberge, marché, garde ?
- Ambiance de jour, de nuit, les jours de fête ?

### Ville
- Quartiers et ce qui les distingue ?
- Fortifications, portes, horaires d'ouverture ?
- Gouvernance, guet, lois locales ?
- Économie, ressources (eau, nourriture), commerce ?

### Région, pays
- Régime politique, capitale, frontières et voisins ?
- Langues, monnaie, religion dominante ?
- Ressources, armée, conflits en cours ?

### Continent
- Pays ou régions qui le composent ?
- Reliefs, climats, routes commerciales ?
- Peuples, et leurs relations ?

### Monde
- Cosmologie : astres, lunes, durée du jour et de l'année, saisons ?
- Calendrier (souvent une fiche système à part) ?
- Continents et océans ?
- Grandes périodes de l'histoire ?

## Approfondissement (optionnel)

Offered after the core; the author picks:

- Histoire : fondation, événements marquants, ruines ?
- Culture : coutumes, fêtes, interdits, cuisine, vêtements ?
- Économie : ce qu'on y produit, achète, vole ?
- Conflits et tensions internes ?
- Secrets du lieu (`{secret}`, `{révélé chN}`) ?
- Détails sensoriels par saison ?
