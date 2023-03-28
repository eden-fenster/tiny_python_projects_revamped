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
from typing import List, Tuple, TextIO

from tabulate import tabulate

default_delimiter: str = ','


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
                        default='inputs/bad-delimiter.tab')

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

    parser.add_argument('-d',
                        '--delimiter',
                        help='change delimiter',
                        metavar='Delimiter',
                        type=str,
                        default=',')

    parser.add_argument('-e',
                        '--easy',
                        help='A boolean flag',
                        action='store_true')

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
    delimiter: str = args.delimiter
    easy: bool = args.easy

    input_file_handle = open("inputs/exercises.csv", "r")
    input_file_handle = io.StringIO("exercise,reps\nBurpees,20-50\n"
                                    "Situps,40-100\nPushups,25-75\n"
                                    "Squats,20-50\nPullups,10-30\n"
                                    "Hand-stand pushups,5-20\nLunges,20-40\n"
                                    "Plank,30-60\nCrunches,20-30")
    reader = csv.DictReader(input_file_handle)
    fieldnames = list(reader.fieldnames)

    output_file_handle = open("output.csv", "w")
    writer = csv.DictWriter(output_file_handle, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()

    for record in reader:
        writer.writerow(record)

    output_file_handle.close()
    input_file_handle.close()

    file_to_read: TextIO = open("output.csv", 'r')
    exercises = read_csv(fh=file_to_read, delimiter=delimiter)

    if not exercises:
        sys.exit(f'No usable data in --file "{file.name}"')

    num_exercises = len(exercises)
    if num > num_exercises:
        sys.exit(f'--num "{num}" > exercises "{num_exercises}"')

    print(print_table(easy=easy, exercises=exercises, num=num))


def print_table(easy: bool, exercises, num: int):
    wod = []
    for name, low, high in random.sample(exercises, k=num):
        reps = random.randint(low, high)
        if easy:
            reps = int(reps / 2)
        wod.append((name, reps))

    return tabulate(wod, headers=('Exercise', 'Reps'))


def read_csv(fh: TextIO, delimiter: str) -> List[Tuple[str, int, int]]:
    """Read the CSV input"""
    exercises = []
    for row in csv.DictReader(fh, delimiter=delimiter):
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
    delimiter = '|'
    assert read_csv(good, delimiter) == [('Burpees', delimiter, 20, delimiter, 50),
                                         ('Situps', delimiter, 40, delimiter, 100)]

    no_data = io.StringIO('')
    assert read_csv(no_data, delimiter) == []

    headers_only = io.StringIO('exercise,reps\n')
    assert read_csv(headers_only, delimiter) == []

    bad_headers = io.StringIO('Exercise,Reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(bad_headers, delimiter) == []

    bad_numbers = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,forty-100')
    assert read_csv(bad_numbers, delimiter) == [('Burpees', delimiter, 20, delimiter, 50)]

    no_dash = io.StringIO('exercise,reps\nBurpees,20\nSitups,40-100')
    assert read_csv(no_dash, delimiter) == [('Situps', delimiter, 40, delimiter, 100)]

    tabs = io.StringIO('exercise\treps\nBurpees\t20-50\nSitups\t40-100')
    assert read_csv(tabs, delimiter) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
