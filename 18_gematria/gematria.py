#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-17
Purpose: Gematria
"""

import argparse
import re

# --------------------------------------------------
import os.path
from typing import List


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text

    for line in text.splitlines():
        split_line: List[str] = line.split()
        for word in split_line:
            word_to_num: str = word2num(word=word)
            print(' '.join(word_to_num))


def word2num(word: str) -> str:
    """Sun the values of all the characters"""
    values = []
    substitute = re.sub('[^A-Za-z0-9]', '', word)
    for char in substitute:
        values.append(ord(char))

    return str(sum(values))


def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
