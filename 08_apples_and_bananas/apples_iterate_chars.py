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
    text: str = args.text
    vowel: str = args.vowel
    new_text = []
    vowels_lower: str = VOWELS.lower()
    vowels_upper: str = VOWELS.upper()

    for char in text:
        if char in vowels_lower:
            new_text.append(vowel)
            continue
        if char in vowels_upper:
            new_text.append(vowel.upper())
            continue
        new_text.append(char)
    text = ''.join(new_text)
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
