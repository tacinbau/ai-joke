# AI joke — make.fun `ai-joke-03`

One one-liner about AI coding agents, written by a tiny Python program.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt (89 bytes, deterministic)
```

`main.py` is Python 3.13 standard library only — no packages, no network.
It writes `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## The joke

> My agent found the bug. It was in the prompt I wrote, which the agent had written for me.

The agent debugs its own instructions and blames you for them.

## Files

- `main.py` — the entry program (the only code file the repo needs).
- `summary.md` — the joke, why it was chosen, validation results.
- `logs/work-log.md` — timestamped build log.
- `LICENSE` — MIT.
