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

    args = parser.parse_args()
    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def int_to_string(bottle: int) -> str:
    digits_dict = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
        9: 'Nine',
    }
    tens_dict = {
        10: 'Ten',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
    }
    teens_dict = {
        11: 'Eleven', 12: 'Twelve',
        13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
        19: 'Nineteen',
    }
    if bottle < 10:
        return digits_dict.get(bottle)

    if 10 < bottle < 20:
        return teens_dict.get(bottle)

    units = bottle % 10
    if units == 0:
        return tens_dict.get(bottle)

    return tens_dict.get(10*int(bottle/10)) + ' ' + digits_dict.get(units)


def verse(bottle: int) -> str:
    """Sing a verse"""
    next_bottle = bottle - 1
    if bottle == 1:
        s1 = ''
    else:
        s1 = 's'

    if next_bottle == 1:
        s2 = ''
    else:
        s2 = 's'

    bottle_word: str = int_to_string(bottle=bottle)

    if next_bottle == 0:
        num_next = 'No more'
    else:
        num_next = int_to_string(bottle=next_bottle)
    return '\n'.join([
        f'{bottle_word} bottle{s1} of beer on the wall,',
        f'{bottle_word} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{num_next} bottle{s2} of beer on the wall!'
    ])


def main():
    """Make a jazz noise here"""
    args = get_args()
    number: int = args.num

    print('\n\n'.join(map(verse, range(number, 0, -1))))


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        'One bottle of beer on the wall,', 'One bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        'Two bottles of beer on the wall,', 'Two bottles of beer,',
        'Take one down, pass it around,',
        'One bottle of beer on the wall!'
    ])

    twenty_two_bottles = verse(22)
    assert twenty_two_bottles == '\n'.join([
        'Twenty Two bottles of beer on the wall,', 'Twenty Two bottles of beer,',
        'Take one down, pass it around,',
        'Twenty One bottles of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
