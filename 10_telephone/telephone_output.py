#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-24
Purpose: Telephone
"""

import argparse
import os
import sys

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

    parser.add_argument('-o',
                        '--outfile',
                        help='Save output to file',
                        type=argparse.FileType('rt'),
                        default=sys.stdout
                        )

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
    mutation: float = args.mutations
    our_text: str = args.text
    output = args.output

    new_text = mutate_text(our_text, mutation, seed)
    print('You said: "{}"\nI heard : "{}"'.format(our_text, ''.join(new_text)), file=output)


def mutate_text(our_text: str, mutation: float, seed: int) -> str:
    random.seed(seed)
    letters_and_punctuations: str = ''.join(sorted(string.ascii_letters + string.punctuation))
    len_text: int = len(our_text)
    mutation_num: int = round(mutation * len_text)
    new_text: list = list(our_text)
    for i in random.sample(range(len_text), mutation_num):
        new_text[i] = random.choice(letters_and_punctuations.replace(new_text[i], ''))
    return ''.join(new_text)


def test_save_to_file():
    text = "Simple text"
    expected_response = "Sikple text"
    response = mutate_text(
        our_text=text,
        mutation=0.1,
        seed=1)
    assert expected_response == response


# --------------------------------------------------
if __name__ == '__main__':
    main()
