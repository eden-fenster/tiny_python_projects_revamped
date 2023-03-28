#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-02
Purpose: Ransom Note
"""

import argparse
import os
import random


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
    if random.choice([0, 1]):
        return char.upper()

    return char.lower()


def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text
    seed: int = args.seed
    random.seed(seed)
    ransom = ''
    for char in text:
        ransom += choose(char)
    print(ransom)


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
