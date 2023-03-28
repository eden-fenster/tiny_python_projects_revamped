#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-12
Purpose: Scramble the letters of words
"""

import argparse

# --------------------------------------------------
import os
import random
import re
from typing import List


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def scramble(word: str) -> str:
    """For words over 3 characters, sort the letters in the middle"""
    regex_word = re.match(r'\w+', word)
    if len(word) > 3 and regex_word:
        middle: List[str] = list(word[1:-1])
        middle.sort()
        word = word[0] + ''.join(middle) + word[-1]

    return word


def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text
    seed: int = args.seed

    random.seed(seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in text.splitlines():
        words: List[str] = []
        split_line: List[str] = splitter.split(line)
        for word in split_line:
            scrambled_word = scramble(word)
            words.append(scrambled_word)
        print(''.join(words))


def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "abcd"
    assert scramble("abcde") == "abcde"
    assert scramble("abcdef") == "abcdef"
    assert scramble("abcde'f") == "a'bcdef"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
