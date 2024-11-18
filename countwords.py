
import re
import sys

from functools import reduce
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

def count_words(file):
    """
    Count the number of times every word in `file` occurs.

    Args:
        file (Path): the file to count the words in

    Returns:
        dict: a mapping of word to count
    """

    all_words = {}

    text = file.read_text()
    words = text.split()

    for word in words:
        #lowercase the word and remove all
        #characters that are not [a-z] or hyphen
        word = word.lower()
        match = re.search(r"([a-z\-]+)", word)

        if match:
            word = match.groups()[0]

            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1

    return all_words


def reduce_dicts(dict1, dict2):
    """
    Combine (reduce) the passed two dictionaries to return
    a dictionary that contains the keys of both, where the
    values are equal to the sum of values for each key
    """

    # explicitly copy the dictionary, as otherwise
    # we risk modifying 'dict1'
    combined = {}

    for key in dict1:
        combined[key] = dict1[key]

    for key in dict2:
        if key in combined:
            combined[key] += dict2[key]
        else:
            combined[key] = dict2[key]

    return combined

if __name__ == "__main__":
    files = sorted(Path("shakespeare").glob("*"))

    with ProcessPoolExecutor() as pool:
        results = pool.map(count_words, files, chunksize=5)

    words = reduce(reduce_dicts, results)

    for key in sorted(words.keys()):
        if words[key] > 2000:
            print(f"{key} == {words[key]}")
