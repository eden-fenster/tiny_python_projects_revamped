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
def fry_single_word(word: str) -> str:
    """Drop 'g' from '-ing' and change 'you' to 'y'all'"""
    ing_word = re.search('(.+)ing$', word)
    you = re.match('([Yy])ou$', word)

    if ing_word:
        prefix = ing_word.group(1)
        if re.search('[aeiouy]', prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"
    elif word == 'think':
        return 'reckon'
    elif word == 'thinking':
        return "reckonin'"
    elif word == 'fixing':
        return "fixin'"

    return word



def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text

    splitter = re.compile(r'(\W+)')
    had_two_word_fry = False
    for line in text.splitlines():
        words: List[str] = []
        raw_words = re.split(splitter, line.rstrip())
        for (count, word) in enumerate(raw_words):
            if had_two_word_fry:
                had_two_word_fry = False
                continue
            two_words = raw_words[count:count+2]
            first_word = two_words[count]
            second_word = two_words[count+1:count+2]
            if first_word == "getting" and second_word == "ready":
                words.append("fixin'")
                had_two_word_fry = True
                continue
            words.append(fry_single_word(word))
        print(''.join(words))


def test_fry():
    assert fry_single_word('you') == "y'all"
    assert fry_single_word('You') == "Y'all"



# --------------------------------------------------
if __name__ == '__main__':
    main()
