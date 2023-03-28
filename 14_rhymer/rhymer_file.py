#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-04
Purpose: Make rhyming "words"
"""

import argparse
import re
import string
import sys


# --------------------------------------------------
from typing import Tuple, List

VOWELS = 'aeiou'

CONSONANTS: str = ''
for c in string.ascii_lowercase:
    if c not in VOWELS:
        CONSONANTS += c

PREFIXES = list(CONSONANTS) + (
    'bl br ch cl cr dr fl fr gl gr pl pr sc '
    'sh sk sl sm sn sp st sw th tr tw thw wh wr '
    'sch scr shr sph spl spr squ str thr').split()


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')
    return parser.parse_args()


# --------------------------------------------------


def stemmer(word: str) -> Tuple[str, str]:
    """Return leading consonants (if any), and 'stem' of words"""
    word = word.lower()

    pattern = (
            '([' + CONSONANTS + ']+)?'  # capture one or more, optional
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


def split_file_into_words(file) -> List[str]:
    words: List[str] = []

    for file_handle in file:
        for line in file_handle.readlines():
            line = line.rstrip()
            new_words_with_punctuation = line.split()
            words = words + new_words_with_punctuation

    new_words: List[str] = []
    for word in words:
        for letter in word:
            if letter in string.punctuation:
                word = word.replace(letter, "")
        new_words.append(word)

    return new_words


def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file

    words: List[str] = split_file_into_words(file=file)

    for word in sorted(words):
        start_of_word, rest_of_word = stemmer(word)
        if not rest_of_word:
            print(f'Cannot rhyme "{word}"')
            continue

        rhyming_words = generate_rhyming_words(rest_of_word, start_of_word)
        formatted_rhyming_words = ' '.join(sorted(rhyming_words))
        print(f'{word} -> {formatted_rhyming_words}')


def generate_rhyming_words(rest_of_word, start_of_word):
    word_with_alternative_prefixes = [prefix + rest_of_word for prefix in PREFIXES if prefix != start_of_word]
    return word_with_alternative_prefixes


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
