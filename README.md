# The World in One Page — Saturday, 21 November 2026

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/dedenabduloh07-ctrl/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/dedenabduloh07-ctrl/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

A newspaper front page that sums up the world's news of Saturday,
21 November 2026, in a single 1024×1024 image. An AI judge that can
see images compares entries two at a time and picks the one that best
sums up the day.

## What the image shows

**Lead story — Russia's biggest strikes hit Kyiv, missiles land in
Poland.** Overnight Russia fired 400+ drones and 110 missiles at
Ukraine, killing 8 people in Kyiv and damaging bridges and railways.
Two Russian missiles and a suspected drone came down in Poland; Warsaw
called it a deliberate provocation.

**Markets — AI sell-off drags the S&P 500 into correction.** The
Nasdaq fell 5.3%, wiping out its 2026 gains, and the Dow followed
into correction territory.

**Justice — World Court: Myanmar guilty of Rohingya genocide.** The
International Court of Justice found Myanmar responsible for genocide
against the Rohingya, the first time any international court has found
a state guilty of genocide.

**Climate — COP31 deadlocked over fossil fuels.** The UN climate talks
in Antalya ran past their deadline as nearly 200 nations split over
fossil fuels.

**Also today:** GTA VI sells $3.8bn in a day; a 6.9 quake shakes
Peru; Houthi missiles fired at Riyadh; the UK and EU sign their
biggest post-Brexit deals.

## How it runs

`main.py` is standard library only. It copies the committed
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
so two runs write identical bytes with no network access.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
