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
        description='Rock the Casbah',
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

    args = get_args()
    text_we_got: str = args.text
    vowel: str = args.vowel
    vowels_lower: str = 'aeiou'
    vowels_upper: str = 'AEIOU'
    text = map(
        lambda c: vowel if c in vowels_lower else vowel.upper()
        if c in vowels_upper else c, text_we_got)

    print(''.join(text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
