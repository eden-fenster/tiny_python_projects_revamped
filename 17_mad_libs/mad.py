#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-15
Purpose: Mad Libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='[str [str ...]]',
                        nargs='*',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs: str = args.inputs
    file = args.file

    text = file.read().rstrip()
    blanks = re.findall('(<([^<>]+)>)', text)

    if not blanks:
        sys.exit(f'"{file.name}" has no placeholders.')

    text = fill_input_from_user(blanks, inputs, text)

    print(text)


def fill_input_from_user(blanks, inputs, text) -> str:
    tmpl = 'Give me {} {}: '
    for placeholder, pos in blanks:
        if pos.lower()[0] in 'aeiou':
            article = 'an'
        else:
            article = 'a'

        if inputs:
            answer = inputs.pop(0)
        else:
            answer = input(tmpl.format(article, pos))

        text = re.sub(placeholder, answer, text, count=1)
    return text


# --------------------------------------------------
if __name__ == '__main__':
    main()
