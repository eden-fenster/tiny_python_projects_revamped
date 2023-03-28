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
    """Drop 'g' from '-ing' and change 'you' to 'y'all'"""
    ing_word = re.search('(.+)ing$', word)
    you = re.match('([Yy])ou$', word)
    your = re.match('([Yy])our$', word)

    if ing_word:
        prefix = ing_word.group(1)
        if re.search('[aeiouy]', prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"
    elif your:
        return your.group(1) + "'all's"

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
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"
    assert fry('your') == "y'all's"
    assert fry('Your') == "Y'all's"


# --------------------------------------------------
if __name__ == '__main__':
    main()
