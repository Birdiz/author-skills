"""Tests for skills/echoes/scripts/echoes.py. Run: python3 -m unittest discover tests"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills/echoes/scripts/echoes.py"
sys.path.insert(0, str(SCRIPT.parent))
import echoes  # noqa: E402

LEXICON = """\
| Terme | Catégorie | Genre | Pluriel | Variantes admises | Fiche |
|---|---|---|---|---|---|
| ombrelin | espèce | m | ombrelins | Ombrelin (en début de phrase) | world/systems/ombrelins.md |
| Porte des Brumes | lieu | f | — | — | world/places/porte-des-brumes.md |
"""

INTENTIONAL = """\
# Échos voulus

## Motifs
- brume — le brouillard du port, voulu

## Refusés
- ch1, l. 3 : « la lanterne éclairait à peine la lanterne voisine » — voulu
"""


def run(chapter, lexicon=None, intentional=None, *extra):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "01.md").write_text(chapter, encoding="utf-8")
        args = [sys.executable, str(SCRIPT), str(tmp / "01.md"), *extra]
        if lexicon:
            (tmp / "LEXICON.md").write_text(lexicon, encoding="utf-8")
            args += ["--lexicon", str(tmp / "LEXICON.md")]
        if intentional:
            (tmp / "intentional.md").write_text(intentional, encoding="utf-8")
            args += ["--intentional", str(tmp / "intentional.md")]
        out = subprocess.run(args, capture_output=True, text=True, check=True).stdout
    return json.loads(out)["chapters"][0]


def families(report, key="echoes"):
    return {e["family"]: e["count"] for e in report[key]}


class Stem(unittest.TestCase):
    def test_gestures_reach_their_stem(self):
        for word, family in [
            ("posa", "pos"), ("posait", "pos"), ("leva", "lev"), ("levé", "lev"),
            ("fixa", "fix"), ("fronça", "fronc"), ("avança", "avanc"),
            ("dévisagea", "dévisag"), ("dévisageait", "dévisag"),
            ("regardé", "regard"), ("regarda", "regard"), ("arrêtée", "arrêt"),
            ("sourit", "souri"), ("souriait", "souri"), ("acquiesça", "acquiesc"),
        ]:
            with self.subTest(word=word):
                self.assertEqual(echoes.stem(word), family)
                self.assertIn(family, echoes.GESTURES)

    def test_short_words_keep_four_letters(self):
        self.assertEqual(echoes.stem("porte"), "port")
        self.assertEqual(echoes.stem("mise"), "mise")


class Words(unittest.TestCase):
    def test_inverted_pronouns_dropped(self):
        self.assertEqual(echoes.words("murmura-t-il, dit-elle, rendez-vous"),
                         ["murmura", "dit", "rendez-vous"])

    def test_elisions_split(self):
        self.assertEqual(echoes.words("jusqu’à l’aube"), ["jusqu", "à", "l", "aube"])


class Analyse(unittest.TestCase):
    def test_headings_not_counted(self):
        report = run("# Chapitre un\n\n# Chapitre deux\n\nIl partit.\n")
        self.assertEqual(report["words"], 2)

    def test_lexicon_masks_whole_phrases_only(self):
        text = ("Il ouvrit la Porte des Brumes. La porte grinça, la porte claqua, "
                "la porte céda. Les ombrelins passaient, les ombrelins criaient.\n")
        report = run(text, LEXICON)
        self.assertEqual(families(report)["port"], 3)
        self.assertNotIn("ombrelin", families(report))

    def test_lexicon_annotations_ignored(self):
        report = run("Au début de la phrase, au début du livre.\n", LEXICON)
        self.assertIn("début", families(report))

    def test_motif_excludes_its_family(self):
        report = run("La brume montait, les brumes couvraient tout, la brume restait.\n",
                     intentional=INTENTIONAL)
        self.assertNotIn("brum", families(report))

    def test_motif_adverb_not_counted(self):
        motif = "## Motifs\n- lentement — le rythme de Mira\n"
        report = run("Elle marchait lentement, très lentement.\n", intentional=motif)
        self.assertEqual(report["ment_adverbs"]["count"], 0)

    def test_refused_row_keeps_its_words(self):
        report = run("La lanterne éclairait à peine la lanterne voisine.\n",
                     intentional=INTENTIONAL)
        self.assertIn("lantern", families(report))

    def test_elided_function_words_not_echoes(self):
        report = run("Il attendit jusqu’à l’aube, jusqu’à la fin, jusqu’à ce que "
                     "quelqu’un vienne. Quelqu’un vint.\n")
        self.assertFalse({"jusqu", "quelqu"} & set(families(report)))

    def test_inverted_verbs_echo(self):
        report = run("— Viens, murmura-t-il.\n— Non, murmura-t-elle.\n")
        self.assertEqual(families(report)["murmur"], 2)

    def test_ment_nouns_not_adverbs(self):
        report = run("Un mouvement, le sentiment, sans mouvement ; il partit lentement.\n")
        self.assertEqual(report["ment_adverbs"]["count"], 1)

    def test_gestures_counted(self):
        text = "Il posa le verre, posa la main, posa le livre, posa la lampe, posa tout.\n"
        report = run(text)
        self.assertEqual(families(report, "gestures")["pos"], 5)


if __name__ == "__main__":
    unittest.main()
