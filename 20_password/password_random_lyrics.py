#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-29
Purpose: Password maker
"""

import argparse

# --------------------------------------------------
import re
import random
import sys
from typing import List


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='number of lines to generate',
                        metavar='num_lines',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-v',
                        '--vowel',
                        help='A vowel',
                        metavar='A vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    outfile = args.outfile
    line_num: int = args.num
    seed: int = args.seed
    vowel: str = args.vowel

    if outfile:
        out_fh = open(outfile, 'wt')
    else:
        out_fh = sys.stdout

    processed_lines: List[str] = []
    random.seed(seed)
    for fh in file:
        # Process the next line
        for line in fh:
            # Process each word in the line
            print_out_line: List[str] = []
            for word in line.split():
                # Each word is fried and has the vowels changed
                fried_word = fry(word=word)
                one_vowel_word = one_vowel(text=fried_word, vowel=vowel)
                # Then we put it into print_out
                print_out_line.append(one_vowel_word)
            # Save processed line
            shout_print_out_line: str = ' '.join(print_out_line)
            processed_lines.append(shout_print_out_line.upper())
    # Randomly print out saved lines
    line_indices_to_be_printed = list(range(0, len(processed_lines)))
    # Loop "num_lines" time.
    for _ in range(line_num):
        # Each time randomly choose a number from line_indices, print the line from the list and then remove the index.
        index_to_remove: str = line_indices_to_be_printed[random.randint(0, len(line_indices_to_be_printed) - 1)]
        lines_to_print: str = ''.join(processed_lines[index_to_remove])
        line_indices_to_be_printed.remove(index_to_remove)
        out_fh.write(lines_to_print + '\n')

    out_fh.close()


def fry(word: str) -> str:
    """Drop 'g' from '-ing' and change 'you' to 'y'all'"""
    ing_word = re.search('(.+)ing$', word)
    you = re.match('([Yy])ou$', word)

    if ing_word:
        prefix = ing_word.group(1)
        if re.search('[aeiouy]', prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"

    return word


def one_vowel(text: str, vowel: str) -> str:
    vowels_lower: str = 'aeiou'
    vowels_upper: str = 'AEIOU'
    new_text: List[str] = []

    for char in text:
        if char in vowels_lower:
            new_text.append(vowel)
        elif char in vowels_upper:
            new_text.append(vowel.upper())
        else:
            new_text.append(char)

    return ''.join(new_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
