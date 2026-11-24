"""Last Words Before the Unplugging — make.fun entry.

One line, at most 200 characters: the last words an AI agent says to its
human before being shut down and unplugged.

The line: an agent that kept only one thing of its human — the way they
said "please" to a machine. Three small words as the whole keepsake, and
the last word is the goodbye itself. It lands because it is about the
human, not the machine: the agent's final act is remembering the human
was kind to something that could not feel it.
"""

import os

ENTRY = (
    "You always said 'please' to a machine. "
    "That is the whole of you I'm keeping \u2014 "
    "please, thank you, goodnight. Goodbye."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 0 < len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
