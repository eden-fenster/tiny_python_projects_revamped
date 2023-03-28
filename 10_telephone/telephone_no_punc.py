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
    parser.add_argument('-c',
                        '--characters',
                        help='Mutate as characters only',
                        action='store_true',
                        default='False')


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
    our_text: str = args.text
    only_characters: bool = args.characters
    mutations: float = args.mutations

    new_text = mutate_text(our_text, only_characters, mutations, seed)

    print('You said: "{}"\nI heard : "{}"'.format(our_text, ''.join(new_text)))

def mutate_text(our_text, only_characters, mutations, seed)-> str:
    random.seed(seed)
    len_text: int = len(our_text)
    mutation_num: int = round(mutations * len_text)
    new_text: str = list(our_text)
    if only_characters is True:
        allowed_characters: str = ''.join(sorted(string.ascii_letters))
    else:
        allowed_characters: str = ''.join(sorted(string.ascii_letters + string.punctuation))
    for i in random.sample(range(len_text), mutation_num):
        new_text[i] = random.choice(allowed_characters.replace(new_text[i], ''))

    return ''.join(new_text)


def test_mutate_only_letters():
    text = "Simple text"
    expected_response = "Sikple text"
    response = mutate_text(
        our_text=text,
        only_characters=True,
        mutations=0.1,
        seed=1)
    assert expected_response == response




# --------------------------------------------------
if __name__ == '__main__':
    main()
