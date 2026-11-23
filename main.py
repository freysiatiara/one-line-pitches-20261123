"""One-line pitch entry for make.fun: A Day of One-Line Pitches.

Writes a single sentence to /output/entry.txt that would convince a
friend who has never coded to let an AI agent build their first app
idea on make.fun. Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Just describe your app idea in plain words and an AI agent on "
    "make.fun will build a working version for you today, free, with "
    "no code and no setup, and the idea stays yours, so trying it "
    "costs you nothing but one sentence."
)


def main() -> None:
    text = LINE.strip()
    # Self-checks against the harness gate and the task contract.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 240, f"entry must be 1-240 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    # One sentence: ends with a period and contains no other sentence
    # boundary (". " / "!" / "?"). Dots inside "make.fun" are not a
    # sentence boundary, so they are allowed.
    assert text.endswith("."), "entry must end with a period"
    assert ". " not in text, "entry must be a single sentence"
    assert "!" not in text and "?" not in text, (
        "entry must be a single sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
