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
    gematria_dictionary: dict = gematria_dict()
    values = []
    substitute = re.sub('[^A-Za-z0-9]', '', word)
    for char in substitute:
        char_value: str = gematria_dictionary.get(char, char)
        values.append(int(char_value))

    return str(sum(values))


def gematria_dict() -> dict:
    letter_dict: dict = {'A': '1', 'a': '1', 'B': '2', 'b': '2', 'C': '3', 'c': '3', 'D': '4', 'd': '4',
                         'E': '5', 'e': '5', 'F': '6', 'f': '6', 'G': '7', 'g': '7', 'H': '8', 'h': '8',
                         'I': '9', 'i': '9', 'J': '10', 'j': '10', 'K': '11', 'k': '11', 'L': '12', 'l': '12',
                         'M': '13', 'm': '13', 'N': '14', 'n': '14', 'O': '15', 'o': '15', 'P': '16', 'p': '16',
                         'Q': '17', 'q': '17', 'R': '18', 'r': '18', 'S': '19', 's': '19', 'T': '20', 't': '20',
                         'U': '21', 'u': '21', 'V': '22', 'v': '22', 'W': '23', 'w': '23', 'X': '24', 'x': '24',
                         'Y': '25', 'y': '25', 'Z': '26', 'z': '26'}
    return letter_dict


def test_word2num():
    """Test word2num"""
    assert word2num("a") == "1"
    assert word2num("abc") == "6"
    assert word2num("ab'c") == "6"
    assert word2num("4a-b'c,") == "10"


# --------------------------------------------------
if __name__ == '__main__':
    main()
