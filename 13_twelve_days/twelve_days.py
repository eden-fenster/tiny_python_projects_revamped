#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-03
Purpose: Twelve Days
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=sys.stdout)
    args = parser.parse_args()
    if args.num not in range(1, 13):
        parser.error(f'--num {args.num} must be between 1 amd 12')
    return args


# --------------------------------------------------
def verse(day: int) -> str:
    """Create a verse"""
    ordinal = {1: 'first', 2: 'second', 3: 'third', 4: 'forth', 5: 'fifth', 6: 'sixth', 7: 'seventh',
               8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}
    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]
    lines = [
        f'On the {ordinal[day]} day of Christmas,''\n'
        f'My true love gave to me,'
    ]

    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


def main():
    """Make a jazz noise here"""

    args = get_args()
    number: int = args.num
    out = args.outfile
    # verses = map(verse, range(1, number + 1))
    verses = [verse(day) for day in range(1, number+1)]
    print('\n\n'.join(verses), file=out)


def test_verse():
    """Test Verse"""
    assert verse(1) == '\n'.join(['On the first day of Christmas,', 'My true love gave to me,',
                                  'A partridge in a pear tree.'])

    assert verse(2) == '\n'.join(['On the second day of Christmas,', 'My true love gave to me,',
                                  'Two turtle doves,', 'And a partridge in a pear tree.'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
