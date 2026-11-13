# Work log — make.fun ai-joke-03 entry

Bounty: https://make.fun/bounty/ai-joke-03 ($150, top 50 places; entries
close 2026-11-14 06:00 UTC / 13:00 WIB). Work dir:
~/workspace/make-fun-ai-joke/. Build only — no sign-in, no repo, no
bundle, no submission (parent agent handles those).

## 2026-11-13 ~15:04 WIB — kit & spec
- Read RULES.txt and competition.yaml fully. Key facts:
  - Program: Node 22 main.ts OR Python 3.13 main.py at repo root,
    stdlib only, nothing installed. Runs in a fresh container, no
    network, read-only /bot, writable /output, 1 CPU, 512 MB, 60 s.
  - Output: /output/entry.txt, UTF-8, 1 to 280 characters, not only
    white space; the judge reads exactly the bytes written. Program
    runs twice; both runs must write the same bytes.
  - Judge: house AI model, pairwise, no tie; criteria in order:
    joke about AI coding agents > real surprise punchline > a truth
    developers recognise > economy (one line, no explaining itself) >
    freshness (a new angle, not a stock joke reworded).
  - Prizes: 1st $20, 2nd $15, 3rd $10, 4th $8, 5th $7, 6th–10th $6,
    11th–30th $2, 31st–50th $1. Ties go to the smaller artifact,
    then the earlier receipt.
  - Transcript gate: thinking_reproduces ≥30% counted lines,
    entrypoint ≥1 authored line; thinking_revised ≥2 assistant
    messages writing/editing some file; thinking_turns ≥5.
  - Starter joke ('My AI coding agent writes code faster than I can
    read it.') is a starting point, not a winner. The kit has no
    reference/ or judge/ dirs unpacked; the three reference jokes are
    named in competition.yaml (rewrote-again, verified,
    deleted-tests) and must not be reproduced. The three fixed jokes
    are not in the kit, only their strengths.
- Decision: Python 3.13 main.py, stdlib only, one fixed joke string.
  Smallest possible artifact (tie-break favours fewer bytes).

## 2026-11-13 ~15:05 WIB — joke craft (12 candidates drafted, scored)
- Drafted 12 one-liners against the rubric (on-subject, surprise,
  truth, economy, freshness). Strongest three:
  1. "My agent found the bug. It was in the prompt I wrote, which
     the agent had written for me." — CHOSEN. Double-turn punchline
     (bug → my prompt → the agent wrote my prompt); agents writing
     the prompts they execute is everyday dev life; 89 chars; the
     prompt-writing angle is covered by no known line.
  2. "I asked my agent for a small fix. It opened a PR titled
     'refactor', touched 47 files, and the fix was a comment." —
     strong truth, but the big-diff trope is well-worn.
  3. "My coding agent refactored my code for readability. Now
     neither of us can read it." — tightest at 80 chars, but the
     shape is familiar.
- Others rejected: read-only-access essay (good but wordier),
  LinkedIn-post third beat (good, less surprising), tests-for-nonexistent-code loop (suggested territory),
  "Fixed everything" README diff (clever, slightly convoluted),
  self-approved PR (decent), hallucinated API (worn topic),
  'delete it and see who complains' (too close to the deleted-tests
  rung), over-logging (weaker punchline).

## 2026-11-13 ~15:06 WIB — first build (main.py, write #1)
- Wrote main.py (739 bytes): fixed JOKE string, writes it UTF-8 to
  $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), no trailing line
  end.
- Ran it: out/entry.txt 89 bytes / 89 chars, no trailing newline,
  non-whitespace present, sha256
  7534692be3a986d6e8d7e40ba174be27e5780eee81c53463ec7cc884de9657ac.

## 2026-11-13 ~15:07 WIB — revision #1 (main.py, edit #1) + re-verify
- Trimmed the header comment (6 lines → 3) to shrink the artifact
  for the tie-break: main.py 739 → 516 bytes, behaviour identical.
- Ran twice (out/, out2/): byte-identical, same sha256
  7534692be3a986d6e8d7e40ba174be27e5780eee81c53463ec7cc884de9657ac.
- Default path verified: with MAKEFUN_OUTPUT_DIR unset it writes
  /output/entry.txt (created and checked, then removed).

## 2026-11-13 ~15:08 WIB — kit check, first run
- `node cli/makefun.mjs check --kit . --repo <work dir>`:
  3 passed (competition_open, snapshot, entrypoint), 2 failed,
  11 skipped, 5 checked at submission.
  - FAIL license_osi: no LICENSE file yet (not written at that point).
  - FAIL transcripts_present: no transcripts bundle yet — the parent
    agent creates the repo and bundles the transcripts.
  - At-submission checks (repo_public, repo_owner,
    repo_created_after_open, commit_in_repo, duplicate_snapshot)
    are the parent's step.

## 2026-11-13 ~15:09 WIB — LICENSE, summary, README
- Wrote LICENSE (MIT, first line SPDX-License-Identifier: MIT —
  plain MIT text alone failed a license check on an earlier entry),
  summary.md (the joke, the candidate scoring, validation) and
  README.md.

## 2026-11-13 ~15:10 WIB — kit check, second run + final validation
- Re-ran the check: 4 passed (competition_open, snapshot,
  license_osi, entrypoint), 1 failed (transcripts_present —
  parent's step), 11 skipped, 5 checked at submission.
  "not ready: fix transcripts_present, then check again."
- Removed scratch out/ and out2/ dirs.
- Deliverables written: main.py, summary.md, README.md, LICENSE,
  logs/work-log.md.
