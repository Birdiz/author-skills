#!/usr/bin/env python3
"""Draw the README images as SVG, in a light and a dark version.

Every word is drawn as outlines from the fonts below, so the images look
the same on every machine: GitHub shows README images through <img>, which
cannot load web fonts. Edit the text in the functions below, then run
`python3 docs/images/build.py`. Needs fonttools and uharfbuzz
(`pip install fonttools uharfbuzz`); the fonts (OFL) are downloaded once
into docs/images/.fonts/.
"""
import io
import os
import urllib.request

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(HERE, ".fonts")
GOOGLE_FONTS = "https://raw.githubusercontent.com/google/fonts/main/ofl/"

# Role: (file in google/fonts, variable axes to pin).
FACES = {
    "serif": ("spectral/Spectral-Regular.ttf", None),
    "italic": ("spectral/Spectral-Italic.ttf", None),
    "bold": ("spectral/Spectral-SemiBold.ttf", None),
    "caps": ("spectralsc/SpectralSC-Medium.ttf", None),
    "hand": ("coveredbyyourgrace/CoveredByYourGrace.ttf", None),
    "mono": ("inconsolata/Inconsolata%5Bwdth%2Cwght%5D.ttf",
             {"wght": 500, "wdth": 100}),
}

# Ink is what the author decides, pencil what a skill suggests.
THEMES = {
    "light": {"ink": "#15171C", "pencil": "#2F5BD3", "graphite": "#5F636C",
              "rule": "#C9CCD2", "paper": "#FFFFFF"},
    "dark": {"ink": "#E6E3DC", "pencil": "#86A6FF", "graphite": "#9BA1AB",
             "rule": "#3A404A", "paper": "#0D1117"},
}


def num(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Face:
    def __init__(self, path, axes):
        font = TTFont(path)
        if axes:
            font = instancer.instantiateVariableFont(font, axes)
        data = io.BytesIO()
        font.save(data)
        self.hb = hb.Font(hb.Face(data.getvalue()))
        self.upem = font["head"].unitsPerEm
        self.glyphs = font.getGlyphSet()
        self.order = font.getGlyphOrder()
        self.paths = {}

    def shape(self, s):
        buf = hb.Buffer()
        buf.add_str(s)
        buf.guess_segment_properties()
        hb.shape(self.hb, buf, {"kern": True, "liga": True})
        return zip(buf.glyph_infos, buf.glyph_positions)

    def width(self, s, size):
        return sum(p.x_advance for _, p in self.shape(s)) * size / self.upem

    def path(self, name):
        """A glyph's outline in font units, y up."""
        if name not in self.paths:
            pen = SVGPathPen(self.glyphs, ntos=num)
            self.glyphs[name].draw(pen)
            self.paths[name] = pen.getCommands()
        return self.paths[name]

    def place(self, s, size, x, y):
        """(glyph name, x, y) for each glyph of s set at (x, y)."""
        scale = size / self.upem
        advance, placed = 0, []
        for info, pos in self.shape(s):
            placed.append((self.order[info.codepoint],
                           x + (advance + pos.x_offset) * scale,
                           y - pos.y_offset * scale))
            advance += pos.x_advance
        return placed


def load_faces():
    os.makedirs(FONTS_DIR, exist_ok=True)
    faces = {}
    for role, (name, axes) in FACES.items():
        path = os.path.join(FONTS_DIR, os.path.basename(name).split("%")[0])
        if not os.path.exists(path):
            urllib.request.urlretrieve(GOOGLE_FONTS + name, path)
        faces[role] = Face(path, axes)
    return faces


class Drawing:
    """Shapes with a colour role, rendered once per theme."""

    def __init__(self, faces, width, height, title, desc):
        self.faces = faces
        self.width, self.height = width, height
        self.title, self.desc = title, desc
        self.items = []

    def measure(self, s, face, size):
        return self.faces[face].width(s, size)

    def text(self, s, face, size, x, y, color="ink", anchor="start"):
        w = self.measure(s, face, size)
        if anchor == "middle":
            x -= w / 2
        elif anchor == "end":
            x -= w
        glyphs = self.faces[face].place(s, size, x, y)
        self.items.append(("text", color, glyphs, (face, size)))
        return x, w

    def runs(self, parts, x, y):
        """Text runs on one baseline: (text, face, size, color) tuples."""
        for s, face, size, color in parts:
            _, w = self.text(s, face, size, x, y, color)
            x += w
        return x

    def wrap(self, s, face, size, width):
        lines, line = [], ""
        for word in s.split():
            test = f"{line} {word}".strip()
            if line and self.measure(test, face, size) > width:
                lines.append(line)
                line = word
            else:
                line = test
        return lines + [line]

    def paragraph(self, s, face, size, x, y, width, leading, color="ink"):
        for line in self.wrap(s, face, size, width):
            self.text(line, face, size, x, y, color)
            y += leading
        return y

    def stroke(self, d, color="ink", width=1.5, dash=None):
        self.items.append(("stroke", color, d, (width, dash)))

    def line(self, x1, y1, x2, y2, color="ink", width=1.5):
        self.stroke(f"M{num(x1)} {num(y1)}L{num(x2)} {num(y2)}", color, width)

    def arrowhead(self, x, y, dx, dy, color="ink", width=2, size=11):
        """Two strokes ending at (x, y), pointing along (dx, dy)."""
        n = (dx * dx + dy * dy) ** 0.5
        ux, uy = dx / n, dy / n
        px, py = -uy, ux
        a = (x - ux * size + px * size * 0.55, y - uy * size + py * size * 0.55)
        b = (x - ux * size - px * size * 0.55, y - uy * size - py * size * 0.55)
        self.stroke(f"M{num(a[0])} {num(a[1])}L{num(x)} {num(y)}"
                    f"L{num(b[0])} {num(b[1])}", color, width)

    def render(self, theme):
        colors = THEMES[theme]
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" '
            f'height="{self.height}" viewBox="0 0 {self.width} {self.height}" '
            f'role="img" aria-labelledby="title desc">',
            f'<title id="title">{self.title}</title>',
            f'<desc id="desc">{self.desc}</desc>',
        ]
        used = {}
        for kind, _, glyphs, style in self.items:
            if kind == "text":
                for name, _, _ in glyphs:
                    used.setdefault((style[0], name), f"g{len(used)}")
        out.append("<defs>")
        for (face, name), gid in used.items():
            out.append(f'<path id="{gid}" d="{self.faces[face].path(name)}"/>')
        out.append("</defs>")
        for kind, color, d, style in self.items:
            if kind == "text":
                face, size = style
                scale = f"{size / self.faces[face].upem:.5f}".rstrip("0")
                out.append(f'<g fill="{colors[color]}">')
                for name, x, y in d:
                    out.append(f'<use href="#{used[(face, name)]}" '
                               f'transform="translate({num(x)} {num(y)}) '
                               f'scale({scale} -{scale})"/>')
                out.append("</g>")
            elif kind == "fill":
                out.append(f'<path fill="{colors[color]}" d="{d}"/>')
            else:
                width, dash = style
                dash = f' stroke-dasharray="{dash}"' if dash else ""
                out.append(
                    f'<path fill="none" stroke="{colors[color]}" '
                    f'stroke-width="{num(width)}" stroke-linecap="round" '
                    f'stroke-linejoin="round"{dash} d="{d}"/>')
        out.append("</svg>")
        return "\n".join(out) + "\n"


def caret(d, x, y, half=9, height=14, width=3.5):
    """The proofreader's insertion mark, its tip at (x, y)."""
    d.stroke(f"M{num(x - half)} {num(y + height)}L{num(x)} {num(y)}"
             f"L{num(x + half)} {num(y + height)}", "pencil", width)


def mark(d, x, y, size, frame=True):
    """The logo: a serif a over an insertion caret, in a square."""
    if frame:
        d.stroke(f"M{num(x)} {num(y)}h{num(size)}v{num(size)}h{num(-size)}z",
                 "ink", size / 45)
    d.text("a", "serif", size * 0.78, x + size / 2, y + size * 0.565,
           anchor="middle")
    caret(d, x + size / 2, y + size * 0.645, half=size * 0.2,
          height=size * 0.15, width=size * 0.05)


def crop_marks(d, x1, y1, x2, y2, length=18, gap=8):
    for x, y, sx, sy in ((x1, y1, -1, -1), (x2, y1, 1, -1),
                         (x1, y2, -1, 1), (x2, y2, 1, 1)):
        d.line(x + sx * gap, y, x + sx * (gap + length), y, "graphite", 1)
        d.line(x, y + sy * gap, x, y + sy * (gap + length), "graphite", 1)


def logo(faces):
    d = Drawing(faces, 512, 512, "author-skills",
                "A serif letter a above a blue proofreader's insertion caret.")
    d.items.append(("fill", "paper", "M0 0h512v512h-512z", None))
    mark(d, 96, 96, 320)
    return d


def banner(faces):
    d = Drawing(faces, 1200, 300, "author-skills",
                "author skills: agent skills for writing a novel. A muse that "
                "never writes for you. The word never is inserted in blue "
                "pencil, like a proofreader's correction.")
    crop_marks(d, 40, 30, 1160, 270)
    mark(d, 96, 104, 104)
    x = 244
    d.text("author skills", "caps", 84, x, 152)
    before = "Agent skills for writing a novel. A muse that"
    after = "writes for you."
    size, gap = 29, 22
    end = d.runs([(before, "serif", size, "ink")], x, 226)
    insert = end + gap / 2
    d.text(after, "serif", size, end + gap, 226)
    d.text("never", "hand", 38, insert, 194, "pencil", anchor="middle")
    caret(d, insert, 222)
    return d


STEPS = [
    ("Set up", ["/setup-novel"],
     "Once. Language, tense, point of view, typography."),
    ("Build", ["/build-character", "/build-world"],
     "Character and world sheets, by interview: your story bible."),
    ("Write", None, "No skill writes a sentence of your novel."),
    ("Revise", ["/scene-breaks", "/echoes", "/proofread"],
     "Scenes, repetitions, strict proofreading. You approve every fix."),
    ("Check", ["/check-continuity"],
     "Contradictions with the bible, quoted. You decide which side is right."),
]


def workflow(faces):
    d = Drawing(faces, 1200, 500, "How you work with author-skills",
                "Five steps: set up once with /setup-novel; build characters "
                "and places with /build-character and /build-world; write, "
                "which only you do; revise with /scene-breaks, /echoes and "
                "/proofread; check continuity with /check-continuity. Then "
                "again, chapter by chapter. When stuck: /brainstorm when an "
                "idea won't take shape, /muse when there is no idea yet.")
    left, top, bottom, col = 40, 120, 392, 224
    d.line(left, top, left + col * 5, top, "ink", 1.5)
    d.line(left, bottom, left + col * 5, bottom, "ink", 1.5)
    for i, (name, commands, desc) in enumerate(STEPS):
        x = left + col * i
        if i:
            d.line(x, top + 14, x, bottom - 14, "rule", 1)
        pad = x + 18
        d.text(str(i + 1), "mono", 15, pad, 152, "graphite")
        d.text(name, "bold" if commands is None else "italic", 32, pad, 194)
        y = 234
        if commands is None:
            for line in ("you, and", "only you"):
                d.text(line, "hand", 32, pad, y + 2, "pencil")
                y += 32
        else:
            for command in commands:
                d.text(command, "mono", 18, pad, y)
                y += 26
        d.paragraph(desc, "serif", 17, pad, y + 12, col - 36, 23, "graphite")
    # Back to writing, above the steps.
    write, check = left + col * 2.5, left + col * 4.5
    d.stroke(f"M{num(check)} {top - 10}C{num(check - 40)} 40 "
             f"{num(write + 40)} 40 {num(write)} {top - 12}", "pencil", 2.5)
    d.arrowhead(write, top - 10, -0.25, 1, "pencil", 2.5)
    d.text("again, chapter by chapter", "hand", 28, (write + check) / 2, 44,
           "pencil", anchor="middle")
    # The way out when stuck, below the steps.
    x, w = d.text("stuck?", "hand", 32, left, 470, "pencil")
    d.stroke(f"M{num(x + w / 2)} 444C{num(x + w / 2)} 420 {num(write - 160)} "
             f"426 {num(write - 6)} {bottom + 10}", "pencil", 2.5)
    d.arrowhead(write - 4, bottom + 9, 0.6, -1, "pencil", 2.5)
    d.runs([
        ("/brainstorm", "mono", 18, "ink"),
        ("  when an idea won't take shape", "serif", 18, "graphite"),
        ("     /muse", "mono", 18, "ink"),
        ("  when there is no idea yet", "serif", 18, "graphite"),
    ], x + w + 24, 468)
    return d


def golden_rule(faces):
    d = Drawing(faces, 1200, 460, "You stay the author",
                "Three steps. A skill proposes: in the line Il regarda le "
                "ciel, the repeated regarda is circled in blue pencil, with "
                "contempla or observa suggested. You decide: you tick "
                "observa, or keep the word as deliberate. Only your yes is "
                "applied: the line becomes Il observa le ciel, and nothing "
                "else changes. No skill writes prose or decides canon.")
    panels = [40, 440, 840]
    titles = ["A skill proposes", "You decide", "Only your yes is applied"]
    for i, (x, title) in enumerate(zip(panels, titles)):
        d.text(str(i + 1), "mono", 15, x, 48, "graphite")
        d.text(title, "italic", 30, x, 90)
        d.line(x, 112, x + 310, 112, "rule", 1)
        if i:
            d.line(x - 62, 196, x - 22, 196, "ink", 1.5)
            d.arrowhead(x - 22, 196, 1, 0, "ink", 1.5, 9)

    # 1. The echo, circled in pencil.
    x = panels[0]
    first = "Il regarda la mer."
    d.text(first, "serif", 26, x, 170)
    d.text("Il regarda le ciel.", "serif", 26, x, 210)
    start = x + d.measure("Il ", "serif", 26)
    word = d.measure("regarda", "serif", 26)
    cx, rx, ry = start + word / 2, word / 2 + 5, 15
    for y in (163, 203):
        d.stroke(f"M{num(cx - rx)} {y + 2}A{num(rx)} {ry} 0 0 0 {num(cx + rx)} {y}"
                 f"A{num(rx)} {ry} 0 0 0 {num(cx - rx + 10)} {y - ry + 4}",
                 "pencil", 2)
    d.line(cx, 163 + ry, cx, 203 - ry, "pencil", 2)
    d.text("echo: regarda, twice", "hand", 28, x, 262, "pencil")
    d.text("contempla?  observa?", "hand", 28, x, 298, "pencil")

    # 2. The author's tick, in ink.
    x = panels[1]
    options = ["contempla", "observa", "keep it, it's deliberate"]
    for j, option in enumerate(options):
        y = 170 + j * 42
        d.stroke(f"M{x} {y - 18}h20v20h-20z", "ink", 1.5)
        d.text(option, "serif", 23, x + 34, y, "ink" if j == 1 else "graphite")
    d.stroke(f"M{x + 2} 199L{x + 9} 209L{x + 26} 182", "ink", 3.2)
    d.paragraph("One click per proposal. Keeping a word on purpose is "
                "remembered, and not asked again.", "serif", 18, x, 290, 320,
                25, "graphite")

    # 3. The corrected line.
    x = panels[2]
    d.text(first, "serif", 26, x, 170)
    end = d.runs([("Il ", "serif", 26, "ink"), ("observa", "bold", 26, "ink")],
                 x, 210)
    d.text(" le ciel.", "serif", 26, end, 210)
    d.line(start - panels[0] + x, 218, end, 218, "ink", 1.5)
    d.paragraph("Nothing else in the chapter is touched.", "serif", 18, x,
                262, 320, 25, "graphite")

    d.line(40, 352, 1160, 352, "ink", 1.5)
    d.text("No skill writes prose. No skill decides canon: when the bible and "
           "the text disagree, you rule.", "serif", 22, 40, 396)
    x = d.runs([("blue pencil", "hand", 26, "pencil"),
                (": what a skill suggests      ", "serif", 18, "graphite")],
               40, 436)
    d.runs([("ink", "bold", 18, "ink"),
            (": what you decide", "serif", 18, "graphite")], x, 436)
    return d


def main():
    faces = load_faces()
    with open(os.path.join(HERE, "logo.svg"), "w") as f:
        f.write(logo(faces).render("light"))
    for name, build in (("banner", banner), ("workflow", workflow),
                        ("golden-rule", golden_rule)):
        drawing = build(faces)
        for theme in THEMES:
            path = os.path.join(HERE, f"{name}-{theme}.svg")
            with open(path, "w") as f:
                f.write(drawing.render(theme))


if __name__ == "__main__":
    main()
