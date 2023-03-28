#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-04
Purpose: Make rhyming "words"
"""

import argparse
import re
import string

# --------------------------------------------------
from typing import Tuple, List, Set


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='words file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='words.txt')

    return parser.parse_args()


VOWELS: str = 'aeiou'


# --------------------------------------------------

def split_word(word: str) -> Tuple[str, str]:
    """Return leading consonants"""
    word = word.lower()

    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in VOWELS])
    pattern = (
            '([' + consonants + ']+)?'  # capture one or more, optional
                                '([' + VOWELS + '])'  # capture at least one vowel
                                                '(.*)'  # capture zero or more of anything
    )

    match = re.match(pattern, word)
    if not match:
        return word, ''
    p1 = match.group(1) or ''
    p2 = match.group(2) or ''
    p3 = match.group(3) or ''
    return p1, p2 + p3


def find_consonant(word: str) -> str:
    """Return leading consonants"""
    consonant, rest_of_word = split_word(word=word)
    _ = rest_of_word
    return consonant


def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file

    # Read in input
    marked_consonants: Set[str] = set()
    # For each line, split into words.
    for line in file.readlines():
        line: str = line.strip()
        line_words = line.split()
        for word in line_words:
            current_consonant = find_consonant(word)

            # For each consonant sounds find, mark that we found it.
            marked_consonants.add(current_consonant)

    # Print out sorted list of consonant sounds found.
    print(sorted(list(marked_consonants)))


# def test_stemmer():
#     """Test stemmer"""
#     assert stemmer('') == ('', '')
#     assert stemmer('cake') == ('c', 'ake')
#     assert stemmer('chair') == ('ch', 'air')
#     assert stemmer('APPLE') == ('', 'apple')
#     assert stemmer('RDNZL') == ('rdnzl', '')
#     assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
