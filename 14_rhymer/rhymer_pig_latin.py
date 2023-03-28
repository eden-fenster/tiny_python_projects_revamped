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
    vowels = 'aeiou'
    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in vowels])
    pattern = (
        '([' + consonants + ']+)?'  # capture one or more, optional
        '([' + vowels + '])'   # capture at least one vowel
        '(.*)'                     # capture zero or more of anything
    )

    match = re.match(pattern, word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return (word, '')


def main():
    """Make a jazz noise here"""

    args = get_args()
    word: str = args.word
    word_in_pig_latin: str = turn_word_into_pig_latin(word)
    print(word_in_pig_latin)


def turn_word_into_pig_latin(word: str) -> str:
    if word.isupper():
        word = word.lower()
    start, rest = stemmer(word)
    end_if_doesnt_start_with_vowel: str = '-ay'
    end_if_start_with_vowel: str = '-yay'
    if rest != word:
        return rest + start + end_if_doesnt_start_with_vowel
    else:
        return word + end_if_start_with_vowel


def test_stemmer():
    """Test stemmer"""
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')

def test_pig_latin():
    assert turn_word_into_pig_latin('') == '-yay'
    assert turn_word_into_pig_latin('cake') == 'akec-ay'
    assert turn_word_into_pig_latin('chair') == 'airch-ay'
    assert turn_word_into_pig_latin('APPLE') == 'apple-yay'
    assert turn_word_into_pig_latin('RDNZL') == 'rdnzl-ay'
    assert turn_word_into_pig_latin('123') == '123-ay'



# --------------------------------------------------
if __name__ == '__main__':
    main()
