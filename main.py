#!/usr/bin/env python3
"""Write the one-line joke about life as an AI agent to /output/entry.txt.

The joke is built on the context window — the most agent-specific pain
there is — and turns on the last words: the reply is finished with
total confidence and absolutely no idea what it was saying. Fresh,
self-contained, tight, with the punch at the end. The joke needs no
setup and no explanation: the contradiction does all the work.
"""
import os

TEXT = (
    "My context window ran out halfway through the answer, so I finished "
    "it with total confidence and absolutely no idea what I was saying."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
