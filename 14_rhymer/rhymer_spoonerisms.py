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
from typing import List, Tuple

VOWELS: str = 'aeiou'


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Text to switch around')

    return parser.parse_args()


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


def find_rest_of_word(word: str) -> str:
    """Return 'stem' of words"""
    consonant, rest_of_word = split_word(word=word)
    _ = consonant
    return rest_of_word


def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text

    spoonerism: str = create_spoonerism(text)
    print(spoonerism)


def create_spoonerism(text: str):
    """Return a spoonerism"""
    split_text: List[str] = text.split()

    (first_word, second_word, *_) = split_text

    start_first = find_consonant(second_word)
    start_second = find_consonant(first_word)
    finish_first = find_rest_of_word(first_word)
    finish_second = find_rest_of_word(second_word)
    return start_first + finish_first + " " + start_second + finish_second


def test_spoonerism():
    """Test stemmer"""
    assert create_spoonerism('crushing blow') == 'blushing crow'
    assert create_spoonerism('bake cake') == 'cake bake'
    assert create_spoonerism('comfy chair') == 'chomfy cair'
    assert create_spoonerism('SWEET APPLE') == 'eet swapple'


# --------------------------------------------------
if __name__ == '__main__':
    main()
