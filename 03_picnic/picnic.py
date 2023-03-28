#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-04
Purpose: Picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic - what to bring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('food',
                        metavar='str',
                        nargs='+',
                        help='what food to bring to the picnic')

    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    parser.add_argument('--use-oxford', action="store_true", default=True)
    parser.add_argument('--seperator', type=str, default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    foods = args.food
    print(args)
    use_oxford = args.use_oxford
    seperator=args.seperator
    num = len(foods)

    if args.sorted:
        foods.sort()

    bringing = ''
    if num == 1:
        bringing = foods[0]
    elif num == 2:
        bringing = ' and '.join(foods)
    else:
        separator_string = f'{seperator} '
        foods[-1] = 'and ' + foods[-1]
        if use_oxford:
            bringing = separator_string.join(foods)
        else:
            bringing = separator_string.join(foods[:-1])+' '+foods[-1]

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
