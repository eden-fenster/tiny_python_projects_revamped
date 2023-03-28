#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-22
Purpose: Create Workout Of (the) Day (WOD)
"""

import argparse
import csv
import io
import random
import sys
import re

# --------------------------------------------------
from typing import List, Tuple

from tabulate import tabulate


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='A boolean flag',
                        action='store_true',
                        default=False)

    parser.add_argument('-t',
                        '--tabulate_design',
                        help='Design of tabulate',
                        metavar='tabulate design',
                        default='plain')

    args = parser.parse_args()
    if args.num < 0:
        parser.error(f'--num {args.num} must be greater than 0')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seed: int = args.seed
    num: int = args.num
    file = args.file
    easy: bool = args.easy
    table_design: str = args.tabulate_design

    exercises = read_csv(fh=file)

    if not exercises:
        sys.exit(f'No usable data in --file "{file.name}"')

    num_exercises = len(exercises)
    if num > num_exercises:
        sys.exit(f'--num "{num}" > exercises "{num_exercises}"')

    wod = []
    for name, low, high in random.sample(exercises, k=num):
        reps = random.randint(low, high)
        if easy:
            reps = int(reps / 2)
        wod.append((name, reps))

    print(tabulate(wod, headers=('Exercise', 'Reps'), tablefmt=table_design))


def read_csv(fh) -> List[Tuple[str, int, int]]:
    """Read the CSV input"""
    exercises = []
    for row in csv.DictReader(fh, delimiter=','):
        name, reps = row.get('exercise'), row.get('reps')
        if name and reps:
            match = re.match(r'(\d+)-(\d+)', reps)
            if match:
                low, high = map(int, match.groups())
                exercises.append((name, low, high))

    return exercises


def test_read_csv():
    """Test read_csv"""

    good = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(good) == [('Burpees', 20, 50), ('Situps', 40, 100)]

    no_data = io.StringIO('')
    assert read_csv(no_data) == []

    headers_only = io.StringIO('exercise,reps\n')
    assert read_csv(headers_only) == []

    bad_headers = io.StringIO('Exercise,Reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(bad_headers) == []

    bad_numbers = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,forty-100')
    assert read_csv(bad_numbers) == [('Burpees', 20, 50)]

    no_dash = io.StringIO('exercise,reps\nBurpees,20\nSitups,40-100')
    assert read_csv(no_dash) == [('Situps', 40, 100)]

    tabs = io.StringIO('exercise\treps\nBurpees\t20-50\nSitups\t40-100')
    assert read_csv(tabs) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
