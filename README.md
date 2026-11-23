# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/patriarkma/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/patriarkma/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

"The World in One Day" — one image summing up the world's news of Sunday 22 November 2026: the COP31 climate summit in Antalya collapses with no deal; Iran hits three tankers in the Strait of Hormuz; a Russian drone strike on flats near Kyiv leaves 14 missing; Mexico captures cartel boss "Chapo Isidro" in a raid that kills 11; the World Court rules Myanmar committed genocide against the Rohingya; a factory fire in Cikande, Indonesia kills 3 with dozens missing; the BepiColombo probe reaches Mercury orbit after eight years; the FBI probes a reported hack of its crime database; and Márquez takes an eighth MotoGP title.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, fully offline, deterministic) copies the front-page image `entry.png` (1024×1024 PNG, 127,515 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.png`, after checking it against the competition gate: PNG format, at most 1 MiB, at most 1024×1024 pixels. Two runs write byte-identical output.

## How the image was made

The front page was drawn for this entry with PIL on the build machine (`draw_image.py`): a masthead naming the day, a lead story on the COP31 collapse, and six more panels covering the day's other top stories, each with its own kicker, headline and summary, plus two briefs in the footer. The submitted program ships the finished image and copies it; the image itself is the entry's picture of the day, judged as a careful picture editor would judge it.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9g59dt7w&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
