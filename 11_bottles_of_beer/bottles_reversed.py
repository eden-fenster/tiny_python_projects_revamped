#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-27
Purpose: Bottles of Beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of Beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    parser.add_argument('-r',
                        '--reverse',
                        help='reverses the order',
                        action='store_true',
                        default=False)

    args = parser.parse_args()
    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------


def verse(bottle: int) -> str:
    """Sing a verse"""
    next_bottle = bottle + 1
    if bottle == 1:
        s1 = ''
    else:
        s1 = 's'

    if next_bottle == 1:
        s2 = ''
    else:
        s2 = 's'

    num = 'No more' if bottle == 0 else bottle
    return '\n'.join([
        f'{num} bottle{s1} of beer on the wall,',
        f'{num} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{next_bottle} bottle{s2} of beer on the wall!'
    ])


def main():
    """Make a jazz noise here"""
    args = get_args()
    number: int = args.num

    print('\n\n'.join(map(verse, range(0, number, 1))))


def test_verse():
    """Test verse"""

    last_verse = verse(0)
    assert last_verse == '\n'.join([
        'No more bottles of beer on the wall,', 'No more bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])

    two_bottles = verse(1)
    assert two_bottles == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        '2 bottles of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
