#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-09
Purpose: Southern fry text
"""

import argparse
import re

# --------------------------------------------------
import os
from typing import List


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def fry(word: str) -> str:
    """Turn 'very' into 'wicked'"""
    very = re.match('([Vv])ery$', word)

    if very:
        return "wicked"

    return word


def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text

    splitter = re.compile(r'(\W+)')
    for line in text.splitlines():
        words: List[str] = []
        for word in re.split(splitter, line.rstrip()):
            words.append(fry(word))
        print(''.join(words))


def test_fry():
    assert fry('very') == "wicked"
    assert fry('Very') == "wicked"



# --------------------------------------------------
if __name__ == '__main__':
    main()
