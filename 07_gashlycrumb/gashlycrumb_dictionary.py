#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-16
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
from typing import Dict, List


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        nargs='+',
                        type=str,
                        help='Word(s) to lookup')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='dictionary.txt')

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    words_we_know: str = args.word

    lookup = {}
    file_handle = open('test_file.txt', 'r')
    lines = file_handle.readlines()
    for line in lines:
        split_line: List[str] = line.split()
        for word in split_line:
            if word == word.upper() and len(word) > 1:
                lookup[word] = line.rstrip()

    print(lookup_words(words_we_know=words_we_know, lookup=lookup))


def lookup_words(words_we_know: str, lookup: Dict) -> str:
    input_to_return: str = ''
    for word in words_we_know:
        if word.upper() in lookup:
            input_to_return += lookup[word.upper()] + '\n'
            continue
        else:
            input_to_return += f'I do not know "{word}".'
    return input_to_return


def test_lookup():
    file_handle = 'test_file.txt'
    lookup = {}
    for line in file_handle:
        lookup[line[0].upper()] = line.rstrip()
    assert lookup_words('appeal', lookup) == 'APPEAL'


# --------------------------------------------------
if __name__ == '__main__':
    main()
