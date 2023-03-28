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
def reverse(word: str) -> str:
    """Reverse the word"""
    reversed_word = word[::-1]
    return reversed_word


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
            reversed_word = reverse(word)
            words.append(reversed_word)
        print(''.join(words))


def test_reverse():
    """Test reverse"""
    state = random.getstate()
    random.seed(1)
    assert reverse("a") == "a"
    assert reverse("ab") == "ba"
    assert reverse("abc") == "cba"
    assert reverse("abcd") == "dcba"
    assert reverse("abcde") == "edcba"
    assert reverse("abcdef") == "fedcba"
    assert reverse("abcde'f") == "f'edcba"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
