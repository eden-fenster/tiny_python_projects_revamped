#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-24
Purpose: Telephone
"""

import argparse
import os


# --------------------------------------------------
import random
import string


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)


    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seed: int = args.seed
    random.seed(seed)
    our_text: str = args.text

    letters_and_punctuations: str = ''.join(sorted(string.ascii_letters + string.punctuation))
    len_text: int = len(our_text)
    mutation_num: int = round(args.mutations * len_text)
    new_text: str = list(our_text)

    for i in random.sample(range(len_text), mutation_num):
        new_text[i] = random.choice(letters_and_punctuations.replace(new_text[i], ''))

    print('You said: "{}"\nI heard : "{}"'.format(our_text, ''.join(new_text)))



# --------------------------------------------------
if __name__ == '__main__':
    main()
