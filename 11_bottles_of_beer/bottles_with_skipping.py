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
    parser.add_argument('-s',
                        '--step',
                        help='How many steps',
                        metavar='Steps',
                        type=int,
                        default=1)

    args = parser.parse_args()
    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')
    if args.step <= 0:
        parser.error(f'--step "{args.step}" must be greater than 0')

    return args


# --------------------------------------------------
def verse(bottle: int, steps: int) -> str:
    """Sing a verse"""
    next_bottle = bottle - steps
    if bottle == 1:
        s1 = ''
    else:
        s1 = 's'

    if next_bottle <= 1:
        s2 = ''
    else:
        s2 = 's'

    num_next = 'No more' if next_bottle <= 0 else next_bottle

    return '\n'.join([
        f'{bottle} bottle{s1} of beer on the wall,',
        f'{bottle} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{num_next} bottle{s2} of beer on the wall!'
    ])


def main():
    """Make a jazz noise here"""
    args = get_args()
    number: int = args.num
    steps: int = args.step

    for i in range(number, 0, -steps):
        print(''.join(verse(i, steps)))
        print()


def test_verse():
    """Test verse"""

    ten_bottles = verse(10, 5)
    assert ten_bottles == '\n'.join([
        '10 bottles of beer on the wall,', '10 bottles of beer,',
        'Take one down, pass it around,',
        '5 bottles of beer on the wall!'
    ])

    four_bottles = verse(4, 2)
    assert four_bottles == '\n'.join([
        '4 bottles of beer on the wall,', '4 bottles of beer,',
        'Take one down, pass it around,',
        '2 bottles of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
