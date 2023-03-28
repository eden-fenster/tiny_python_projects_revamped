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
from typing import List, Tuple
VOWELS: str = 'aeiou'


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
    two_brackets = re.findall('[...]', text)
    one_left_bracket = re.findall('[[^]]', text)
    one_right_bracket = re.findall('[^[]]', text)
    two_curly_brackets = re.findall('{...}', text)
    one_left_curly_bracket = re.findall('{[^}]', text)
    one_right_curly_bracket = re.findall('[^{]}', text)
    two_parenthesis = re.findall('(...)', text)
    one_left_parenthesis = re.findall('{[^)]', text)
    one_right_parenthesis = re.findall('[^(]}', text)

    if not two_brackets and not one_left_bracket and not one_right_bracket and not two_curly_brackets and not one_left_curly_bracket and not one_right_curly_bracket and not two_parenthesis and not one_left_parenthesis and not one_right_parenthesis:
        sys.exit(f'"{file.name}" has no placeholders.')

    text_two_brackets = replace_placeholders(placeholders=two_brackets, inputs=inputs, text=text)
    text_one_left_bracket = replace_placeholders(placeholders=one_left_bracket, inputs=inputs, text=text_two_brackets)
    text_one_right_bracket = replace_placeholders(placeholders=one_right_bracket,
                                                  inputs=inputs,
                                                  text=text_one_left_bracket)
    text_two_curly_brackets = replace_placeholders(placeholders=two_curly_brackets,
                                                   inputs=inputs,
                                                   text=text_one_right_bracket)
    text_one_left_curly_bracket = replace_placeholders(placeholders=one_left_curly_bracket,
                                                       inputs=inputs,
                                                       text=text_two_curly_brackets)
    text_one_right_curly_bracket = replace_placeholders(placeholders=one_right_curly_bracket,
                                                        inputs=inputs,
                                                        text=text_one_left_curly_bracket)
    text_two_parenthesis = replace_placeholders(placeholders=two_parenthesis,
                                                inputs=inputs,
                                                text=text_one_right_curly_bracket)
    text_one_left_parenthesis = replace_placeholders(placeholders=one_left_parenthesis,
                                                     inputs=inputs,
                                                     text=text_two_parenthesis)
    text_one_right_parenthesis = replace_placeholders(placeholders=one_right_parenthesis,
                                                      inputs=inputs,
                                                      text=text_one_left_parenthesis)

    print(text_one_right_parenthesis)


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
