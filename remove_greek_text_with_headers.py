"""Module for regular expression"""

import re


def convert_to_markdown(input_file, output_file):
    verse_header_pattern = re.compile(r"^(\d+):(\d+)\s+a\.\s+(.+)$")
    verse_subline_pattern = re.compile(r"^\s*([a-z])\.\s+(.+)$")

    verses = {}
    current_verse_num = None

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")

            # Check if this line is a new verse header with 'a.' line
            header_match = verse_header_pattern.match(line)
            if header_match:
                verse_num = header_match.group(2)
                text = header_match.group(3)
                current_verse_num = verse_num
                verses[current_verse_num] = [f"a. {text}"]
                continue

            # Check if line is a subline (b., c., d., etc.) belonging to current verse
            subline_match = verse_subline_pattern.match(line)
            if subline_match and current_verse_num is not None:
                letter = subline_match.group(1)
                text = subline_match.group(2)
                verses[current_verse_num].append(f"{letter}. {text}")
                continue

            # If neither header nor subline, skip line

    with open(output_file, "w", encoding="utf-8") as f_out:
        for vnum in sorted(verses, key=lambda x: int(x)):
            f_out.write(f"###### v{vnum}\n")
            for verse_line in verses[vnum]:
                f_out.write(verse_line + "\n")
            f_out.write("\n")  # blank line after each verse


# Example call:
convert_to_markdown("Bible verse formatting/Raw verses/John-17.txt", "Bible verse formatting/Cleaned verses/John-17.md")
