"""One-Line Roast entry: writes a single roast line to /output/entry.txt.

Deterministic, no network, no arguments, no dependencies.
The line below was chosen from 36 original candidates through blind
two-way duels judged against the competition's published judge criteria
(see FORGE.md in the workspace for candidates and duel scores).
"""

import os

ENTRY = "My washing machine finishes, then beeps every thirty seconds until I come and applaud it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
