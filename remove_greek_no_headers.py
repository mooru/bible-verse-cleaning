"""Module for regular expression"""

import re


def is_english_line(line):
    stripped = line.strip()
    # Check if line is verse header (e.g. '16:5') or subline (a., b., etc.)
    return re.match(r"^\d+:\d+", stripped) or re.match(  # verse line like 16:5
        r"^[a-z]\.", stripped
    )  # a., b., etc.


def clean_and_group(input_path, output_path):
    verses = {}
    current_verse = None

    with open(input_path, "r", encoding="utf-8") as infile:
        for raw_line in infile:
            line = (
                raw_line.strip()
            )  # remove all leading/trailing whitespace including indentation

            if not is_english_line(line):
                continue  # skip lines that aren't English verse lines or sublines

            # Check if line is a verse header like 16:5 a. ...
            verse_header_match = re.match(r"^(\d+:\d+)\s+a\.\s+(.+)$", line)
            if verse_header_match:
                current_verse = verse_header_match.group(1)  # e.g. '16:5'
                first_subline = f"a. {verse_header_match.group(2)}"
                verses[current_verse] = [first_subline]
                continue

            # Otherwise it should be a subline like 'b. ...', 'c. ...'
            subline_match = re.match(r"^([a-z]\.)\s+(.+)$", line)
            if subline_match and current_verse:
                verses[current_verse].append(
                    f"{subline_match.group(1)} {subline_match.group(2)}"
                )

    # Write to output with blank line between verses
    with open(output_path, "w", encoding="utf-8") as outfile:
        for verse_num in sorted(
            verses, key=lambda x: (int(x.split(":")[0]), int(x.split(":")[1]))
        ):
            outfile.write(f"{verse_num} " + verses[verse_num][0] + "\n")
            for subline in verses[verse_num][1:]:
                outfile.write(subline + "\n")
            outfile.write("\n")  # blank line between verses


# Usage
input_file = "bible.txt"
output_file = "output.md"
clean_and_group(input_file, output_file)
