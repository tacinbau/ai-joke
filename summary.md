# AI joke — method summary

Bounty: make.fun `ai-joke-03` ($150; prizes 1st $20, 2nd $15, 3rd $10,
4th $8, 5th $7, 6th–10th $6, 11th–30th $2, 31st–50th $1; entries close
2026-11-14 06:00 UTC / 13:00 WIB).
Entry program: `main.py` (Python 3.13, standard library only), writes
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## The joke

> My agent found the bug. It was in the prompt I wrote, which the agent had written for me.

89 characters, no trailing line end.

## Why this joke (judge criteria, in order)

1. **On subject:** it is unmistakably a joke about working with an AI
   coding agent — "my agent", "the bug", "the prompt".
2. **Surprise:** the punchline turns twice. First the bug is in *my*
   prompt (the human is at fault after all); then the prompt itself was
   written by the agent — so the agent debugged its own work and blamed
   me for it.
3. **Truth:** agents writing the prompts they then execute is everyday
   dev life now, and every developer who works beside one recognises the
   loop: you paste in what the agent wrote, something breaks, and the
   agent helpfully explains that your instructions were wrong.
4. **Economy:** 89 characters, three short sentences, nothing wasted;
   no setup is explained, the twist lands in the last five words.
5. **Freshness:** none of the kit's known lines covers the
   prompt-writing angle — not the starter ("writes code faster than I
   can read it"), not the three reference jokes (rewrote-again,
   verified, deleted-tests). The angle is the agent debugging its own
   instructions, not the usual over-eager rewrite, fake verification,
   or deleted tests.

## Candidates considered

Twelve one-liners were drafted and scored against the rubric; the
runners-up were: "I asked my agent for a small fix. It opened a PR
titled 'refactor', touched 47 files, and the fix was a comment."
(strong truth, but the big-diff trope is well-worn) and "My coding
agent refactored my code for readability. Now neither of us can read
it." (tightest at 80 characters, but the shape is familiar). The
chosen joke beat both on surprise — a double turn instead of a single
one — and on freshness.

## How the program works

`main.py` holds the joke as one fixed string and writes it, UTF-8, to
`entry.txt` in `$MAKEFUN_OUTPUT_DIR` (default `/output`). No network,
no randomness, no time, no input read — two runs write byte-identical
files. The program is 516 bytes (ties go to the smaller artifact).

## Validation

- Gate rules: UTF-8, 89 characters (limit 280), not only white space,
  no trailing line end.
- Deterministic: two runs byte-identical (sha256
  `7534692be3a986d6e8d7e40ba174be27e5780eee81c53463ec7cc884de9657ac`).
- Default output path verified: with `MAKEFUN_OUTPUT_DIR` unset it
  writes `/output/entry.txt` (created and checked, then removed).
- Runtime well under 1 s (limit 60 s), 1 CPU, far under 512 MB.
- `makefun check` (run before LICENSE was written): pass
  competition_open, snapshot, entrypoint; FAIL license_osi (no LICENSE
  file yet) and transcripts_present (no transcripts bundle yet — the
  parent agent creates the repo and bundles the transcripts). Re-run
  after LICENSE was added: license_osi passes.

## Files

- `main.py` — the entry program (writes the joke; the only file the
  repo needs besides LICENSE).
- `summary.md`, `README.md`, `LICENSE` (MIT), `logs/work-log.md`.
