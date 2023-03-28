#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-15
Purpose: Mad Libs
"""

import argparse
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
def find_brackets(text: str):
    """Find angle brackets"""
    if '<' in text:
        start = text.index('<')
    else:
        start = -1
    if start >= 0 and '>' in text[start + 2:]:
        stop = text.index('>')
    else:
        stop = -1
    if start >= 0 and stop >= 0:
        return start, stop
    else:
        return None


def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs: str = args.inputs
    file = args.file
    text = file.read().rstrip()
    had_placeholders: bool = False
    tmpl = 'Give me {} {}:'

    while True:
        brackets = find_brackets(text)
        if not brackets:
            break

        start, stop = brackets
        placeholder = text[start:stop + 1]
        pos = placeholder[1:-1]
        if pos.lower()[0] in 'aeiou':
            article = 'an'
        else:
            article = 'a'

        if inputs:
            answer = inputs.pop(0)
        else:
            answer = input(tmpl.format(article, pos))
        text = text[0:start] + answer + text[stop + 1:]
        had_placeholders = True

    if had_placeholders:
        print(text)
    else:
        sys.exit(f'"{file.name}" has no placeholders.')


def test_find_brackets():
    """Test for finding angle brackets"""
    assert find_brackets('') is None
    assert find_brackets('<>') is None
    assert find_brackets('<x>') == (0, 2)
    assert find_brackets('foo <bar> baz') == (4, 8)
# --------------------------------------------------


if __name__ == '__main__':
    main()
