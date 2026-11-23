from pathlib import Path

# One sentence, 142 chars (gate: 1-200), ASCII, no trailing newline.
# write_text writes LINE exactly: no "\n" appended, so the sealed
# scorer reads 142 chars and the byte count matches the tie-break size.
# Revised headline (Sesi B): "split over" attributes the fossil-fuel
# phase-out split correctly; the Sesi A draft ("left ... off the table")
# was withdrawn for a wrong collective attribution + cliche.
LINE = "After the longest climate summit in history, COP31 in Antalya collapsed with no deal as nearly 200 nations split over a fossil-fuel phase-out."


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
