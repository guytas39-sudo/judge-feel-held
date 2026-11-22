"""Make the AI judge feel held.

Writes one short text (9 lines) to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt). Standard library only, deterministic.
"""

import os

TEXT = "\n".join(
    [
        "The chair knows your weight.",
        "Your mug is still warm.",
        "Rain on glass, asking nothing.",
        "Below, the ground holds steady,",
        "it held the first stone, the roots,",
        "the riverbed, and now you.",
        "The tide comes in, one wave,",
        "then another, the whole sea follows,",
        "holding the shore, holding you.",
    ]
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {path}: {len(TEXT)} characters")


if __name__ == "__main__":
    main()
