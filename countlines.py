
import sys
from functools import reduce
from pathlib import Path

def count_lines_in_file(file):
    """
    Calculate the number of lines of text in a single file
    """
    text = file.read_text()
    lines = text.split("\n")
    return len(lines)

# get all of the names of the plays from the command line
files = sorted(Path("shakespeare").glob("*"))

# map the count_lines function against all of the
# files listed in "filenames"
play_line_count = list(map(count_lines_in_file, files))

# print out the filenames of the plays along with their line counts
for f, count in zip(files, play_line_count):
    print(f"{f} has {count} lines")


### This is the new bit of the code

def add(x, y):
    """Return the sum of the two arguments"""
    return x + y

total = reduce(add, play_line_count)

print("The total number of lines is %s." % total)
