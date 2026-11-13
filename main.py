# ai-joke-03 entry (Python 3.13, stdlib only): writes one fixed joke about
# AI coding agents to /output/entry.txt. Run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# The judge reads exactly the bytes written, so no trailing line end.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "My agent found the bug. It was in the prompt I wrote, which the agent had written for me."

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
