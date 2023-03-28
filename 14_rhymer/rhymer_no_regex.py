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
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def stemmer(word: str):
    """Return leading consonants (if any), and 'stem' of words"""
    word = word.lower()
    vowel_pos = list(map(word.index, filter(lambda v : v in word, 'aeiou')))

    if vowel_pos:
        first_vowel = min(vowel_pos)
        return (word[:first_vowel], word[first_vowel:])
    else:
        return (word, '')


def main():
    """Make a jazz noise here"""

    args = get_args()
    word: str = args.word

    consonants: str = ''
    for c in string.ascii_lowercase:
        if c not in 'aeiou':
            consonants += c

    prefixes = list(consonants) + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()
    start, rest = stemmer(word)
    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{word}"')


def test_stemmer():
    """Test stemmer"""
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
