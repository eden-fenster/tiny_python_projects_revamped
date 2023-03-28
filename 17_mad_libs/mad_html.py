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
from typing import Tuple, List

VOWELS = 'aeiou'


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'))

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

    original_text = file.read().rstrip()
    placeholders_regular = re.findall('(<([^<>]+)>)', original_text)
    placeholders_special = re.findall('(</([^<>]+)>)', original_text)

    if not placeholders_regular and not placeholders_special:
        sys.exit(f'"{file.name}" has no placeholders.')

    text_special = replace_placeholders(placeholders=placeholders_special, inputs=inputs, text=original_text)
    final_text = replace_placeholders(placeholders=placeholders_regular, inputs=inputs, text=text_special)

    print(final_text)


def replace_placeholders(placeholders: List[Tuple[str, str]], inputs, text) -> str:
    for placeholder, original_token in placeholders:
        replacement = get_replacement(inputs=inputs, original_token=original_token)

        text = re.sub(placeholder, replacement, text, count=1)
    return text


def get_replacement(inputs: List[str], original_token: str):
    question_template = 'Give me {} {}: '
    article = method_name(original_token)
    if inputs:
        return inputs.pop(0)

    replacement = input(question_template.format(article, original_token))
    return replacement


def method_name(pos):
    if pos.lower()[0] in VOWELS:
        return 'an'
    return 'a'


# --------------------------------------------------
if __name__ == '__main__':
    main()
