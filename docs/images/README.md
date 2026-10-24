# Images

The README's images, drawn by [build.py](build.py) in a light and a dark
version (`<name>-light.svg`, `<name>-dark.svg`); the README picks one with
`<picture>` and GitHub's theme. `logo.svg` has its own white ground and
serves both themes, and as the repository's avatar.

## The look

A printer's proof: black ink on white paper, and a proofreader's blue
pencil. Ink is what the author decides; blue pencil is what a skill
suggests. The logo is a serif *a* over the insertion caret.

| Role     | Light     | Dark      |
|----------|-----------|-----------|
| ink      | `#15171C` | `#E6E3DC` |
| pencil   | `#2F5BD3` | `#86A6FF` |
| graphite | `#5F636C` | `#9BA1AB` |
| rule     | `#C9CCD2` | `#3A404A` |

Fonts (all under the SIL Open Font License): Spectral for text, Spectral SC
for the name, Inconsolata for commands, Covered By Your Grace for the
pencil.

## Changing an image

Edit the text or the layout in `build.py`, then:

```
pip install fonttools uharfbuzz
python3 docs/images/build.py
```

Words are drawn as outlines, since an `<img>` cannot load web fonts, so
the SVG files are not edited by hand. The fonts are downloaded from
google/fonts into `docs/images/.fonts/` on the first run.
