#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-02
Purpose: Ransom Note
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        help='Random seed',
                        type=int,
                        default=None)
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def choose(char):
    """Randomly choose an upper or lowercase letter to return"""
    letters_and_punctuations: str = string.ascii_letters + string.punctuation
    if random.choice([0, 1]):
        new_char = random.choice(letters_and_punctuations.replace(char, ''))
        return new_char
    else:
        return char.lower()


def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text
    seed: int = args.seed
    our_text = mutate_ransom(text, seed)
    print(our_text)


def mutate_ransom(text: str, seed: int) -> str:
    random.seed(seed)
    ransom = []
    for char in text:
        ransom.append(choose(char))
    return ''.join(ransom)


def test_mutate_ransom():
    text = "Simple text"
    expected_response = "siq'Xe d%xJ"
    response = mutate_ransom(text=text,
                             seed=1)
    assert expected_response == response


def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'c'
    assert choose('d') == 'd'
    random.setstate(state)




# --------------------------------------------------
if __name__ == '__main__':
    main()
