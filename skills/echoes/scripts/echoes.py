#!/usr/bin/env python3
"""Count lexical echoes and tics in French chapters.

Prints JSON: per chapter, echoes (one word family repeated within a
short window), concentrations (a family dense over a passage), overused
families, gesture verbs, weak verbs and -ment adverbs;
across chapters, the families dense in most of them. Families come from a
light suffix-stripping stemmer, so a family can merge homographs
(« porte », « porta »): the agent judges every candidate.
"""
import argparse
import json
import re
from collections import defaultdict

WORD = re.compile(r"[a-zàâäçéèêëîïôöùûüœæ]+(?:-[a-zàâäçéèêëîïôöùûüœæ]+)*")

STOP = set("""
alors après aussi autre autres avant avec avoir bien cela celle celles celui
cependant ceci certain chaque comme comment dans depuis donc dont elle elles
encore entre être était étaient avait avaient fois jamais leur leurs lorsque
mais même moins notre nous parce pendant peut plus plusieurs pour pourquoi
quand quel quelle quelles quels quelque quelques sans sera seulement sinon
sont sous tandis tant toujours tout toute toutes tous très trop vers votre
vous voilà ainsi assez aucun aucune avoir déjà ensuite enfin presque puis
rien cette celui-ci celle-ci là-bas peut-être
deux trois quatre cinq sept huit neuf vingt trente quarante cent mille
premier première second seconde dernier dernière
contre devant derrière près loin autour dessus dessous parmi selon
""".split())

# Verbs that punctuate action between replies.
GESTURES = {
    "regard", "arrêt", "pos", "hoch", "tourn", "retourn", "lev", "baiss",
    "souri", "soupir", "haus", "fronc", "pliss", "hésit", "recul", "avanc",
    "approch", "fix", "dévisag", "tois", "tapot", "serr", "croisa", "crois",
    "hauss", "secou", "inclin", "acquiesç", "acquiesc",
}
WEAK_FORMS = {
    "faire": {"faire", "fait", "faits", "faite", "faites", "fais", "faisait",
              "faisaient", "fit", "firent", "ferait", "feraient", "fera"},
    "mettre": {"mettre", "mit", "mirent", "mettait", "mettaient", "mis",
               "mise", "mises", "mettra"},
    "sembler": {"sembla", "semblait", "semblaient", "sembler", "semble",
                "semblèrent", "semblant"},
    "commencer à": {"commença", "commençait", "commencèrent", "commencer"},
    "chose": {"chose", "choses"},
}

SUFFIXES = sorted("""
èrent erent aient eraient issaient issait issant irent assent asse
ait ais ant ante antes ants ions iez ons ent ées ée és er ez ir it is
a e s x
""".split(), key=len, reverse=True)


def stem(word):
    if word.endswith("ment") and len(word) > 7:
        return word  # adverbs counted on their own
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def lexicon_terms(path):
    terms = set()
    if not path:
        return terms
    try:
        for line in open(path, encoding="utf-8"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5 or cells[0] in ("Terme", "") or set(cells[0]) <= {"-"}:
                continue
            for term in [cells[0]] + cells[4].split(","):
                terms.update(w.lower() for w in WORD.findall(term.lower()))
    except FileNotFoundError:
        pass
    return terms


def intentional_words(path):
    words = set()
    if path:
        try:
            for line in open(path, encoding="utf-8"):
                words.update(WORD.findall(line.lower().split("—")[0]))
        except FileNotFoundError:
            pass
    return words


def proper_nouns(paths, scene_break):
    """Words capitalised in most of their mid-sentence occurrences."""
    caps, total = defaultdict(int), defaultdict(int)
    for path in paths:
        for line in open(path, encoding="utf-8"):
            if line.strip() == scene_break:
                continue
            for m in re.finditer(r"(?<=[\w,;:] )([A-Za-zÀ-ÿœæ]+)", line.replace("’", "'")):
                w = m.group(1)
                total[w.lower()] += 1
                caps[w.lower()] += w[0].isupper()
    return {w for w, t in total.items() if t and caps[w] / t >= 0.8}


def tokens(path, scene_break):
    out = []
    for n, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if not line.strip() or line.strip() == scene_break:
            continue
        dialogue = line.lstrip()[:1] in "—–-"
        text = line.lower().replace("’", "'")
        for w in WORD.findall(text.replace("'", " ")):
            out.append((w, n, dialogue))
    return out


def analyse(path, a, excluded):
    toks = tokens(path, a.scene_break)
    words = len(toks)
    by_family = defaultdict(list)
    for i, (w, n, dialogue) in enumerate(toks):
        if len(w) < 4 or w in STOP or w in excluded:
            continue
        by_family[stem(w)].append((i, w, n, dialogue))

    echoes = []
    for fam, occ in by_family.items():
        run = [occ[0]]
        for o in occ[1:] + [None]:
            if o is not None and o[0] - run[-1][0] <= a.window:
                run.append(o)
                continue
            if len(run) >= 2:
                echoes.append({
                    "family": fam, "count": len(run),
                    "forms": sorted({r[1] for r in run}),
                    "lines": [r[2] for r in run],
                    "closest": min(y[0] - x[0] for x, y in zip(run, run[1:])),
                    "in_dialogue": sum(r[3] for r in run),
                })
            run = [o] if o is not None else []
    echoes.sort(key=lambda e: (-e["count"], e["closest"]))

    zones = []
    for fam, occ in by_family.items():
        best, start = [], 0
        for end in range(len(occ)):
            while occ[end][0] - occ[start][0] > a.zone:
                start += 1
            if end - start + 1 > len(best):
                best = occ[start:end + 1]
        if len(best) >= a.zone_count:
            zones.append({"family": fam, "count": len(best),
                          "forms": sorted({x[1] for x in best}),
                          "lines": [x[2] for x in best],
                          "span_words": best[-1][0] - best[0][0]})
    zones.sort(key=lambda z: (-z["count"], z["span_words"]))

    per_k = lambda c: round(1000 * c / max(words, 1), 1)
    overuse = sorted(
        ({"family": f, "count": len(o), "per_1000": per_k(len(o)),
          "forms": sorted({x[1] for x in o}), "lines": sorted({x[2] for x in o})}
         for f, o in by_family.items() if len(o) >= a.min_count),
        key=lambda x: -x["count"])

    gestures = [g for g in overuse if g["family"] in GESTURES]
    weak = []
    for verb, forms in WEAK_FORMS.items():
        hits = [(w, n) for w, n, _ in toks if w in forms]
        if hits:
            weak.append({"verb": verb, "count": len(hits), "per_1000": per_k(len(hits)),
                         "lines": sorted({n for _, n in hits})})
    adverbs = [(i, w, n) for i, (w, n, _) in enumerate(toks) if w.endswith("ment") and len(w) > 7
               and w not in excluded]
    clusters = []
    for x, y in zip(adverbs, adverbs[1:]):
        if y[0] - x[0] <= a.window // 2:
            clusters.append({"words": [x[1], y[1]], "lines": [x[2], y[2]]})

    return {
        "file": path, "words": words, "echoes": echoes[: a.top],
        "concentrations": zones[: a.top],
        "overuse": overuse[: a.top], "gestures": gestures, "weak_verbs": weak,
        "ment_adverbs": {"count": len(adverbs), "per_1000": per_k(len(adverbs)),
                         "clusters": clusters},
    }, {f: per_k(len(o)) for f, o in by_family.items()}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("chapters", nargs="+")
    p.add_argument("--lexicon")
    p.add_argument("--intentional")
    p.add_argument("--scene-break", default="* * *")
    p.add_argument("--window", type=int, default=50, help="words between two occurrences of an echo")
    p.add_argument("--zone", type=int, default=400, help="words of a concentration window")
    p.add_argument("--zone-count", type=int, default=4, help="occurrences that make a concentration")
    p.add_argument("--min-count", type=int, default=5)
    p.add_argument("--top", type=int, default=25)
    a = p.parse_args()

    excluded = (lexicon_terms(a.lexicon) | intentional_words(a.intentional)
                | proper_nouns(a.chapters, a.scene_break))
    chapters, densities = [], []
    for path in a.chapters:
        report, density = analyse(path, a, excluded)
        chapters.append(report)
        densities.append(density)

    novel = []
    if len(chapters) >= 2:
        families = set().union(*densities)
        for f in families:
            values = [d.get(f, 0) for d in densities]
            dense = sum(v >= 1.5 for v in values)
            if dense >= max(2, round(0.66 * len(values))):
                novel.append({"family": f, "per_1000_by_chapter": values,
                              "gesture": f in GESTURES})
        novel.sort(key=lambda x: -sum(x["per_1000_by_chapter"]))
    json.dump({"chapters": chapters, "novel": novel[: a.top]}, __import__("sys").stdout,
              ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
