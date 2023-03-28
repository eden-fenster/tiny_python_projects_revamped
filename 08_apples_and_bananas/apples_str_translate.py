#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-19
Purpose: Apples and Bananas
"""

import argparse
import os


# --------------------------------------------------
import os.path


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='Input text or file',)

    parser.add_argument('-v',
                        '--vowel',
                        help='A vowel',
                        metavar='A vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))


    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    VOWELS: str = "aeiou"
    args = get_args()
    vowel: str = args.vowel
    vowels: str = VOWELS.lower()+VOWELS.upper()
    trans = str.maketrans(vowels, vowel * len(VOWELS) + vowel.upper() * len(VOWELS))
    text=args.text.translate(trans)
    print(text)




# --------------------------------------------------
if __name__ == '__main__':
    main()
