#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-29
Purpose: Password maker
"""

import argparse

# --------------------------------------------------
import re
import random
import string
from typing import List


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='number of words to use in a password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_length',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_length',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    num_passwords: int = args.num
    num_words: int = args.num_words
    min_words: int = args.min_word_length
    max_words: int = args.max_word_length
    l33t_flag: bool = args.l33t
    seed: int = args.seed

    random.seed(seed)
    words: set = set()

    for fh in file:
        for line in fh:
            for word in line.lower().split():
                if not is_length_ok(minimum=min_words, word=word, maximum=max_words):
                    continue
                word_with_capital: str = str.title(word)
                clean_word: str = clean(word=word_with_capital)
                words.add(clean_word)
    sorted_words: List[str] = sorted(words)
    for _ in range(num_passwords):
        new_password: str = ''.join(random.sample(sorted_words, num_words))
        if l33t_flag is True:
            print(l33t(text=new_password))
        else:
            print(new_password)


def clean(word: str) -> str:
    """Clean out word from non word characters"""
    return re.sub('[^a-zA-Z]', '', word)


def is_length_ok(minimum: int, word: str, maximum: int) -> bool:
    return minimum <= len(word) <= maximum


def l33t(text: str) -> str:
    text = ransom(text)
    xform = str.maketrans({
        'a': '@', 'A': '4', 'O': 'o', 't': '+', 'E': '3', 'I': '1', 'S': '5'
    })
    return text.translate(xform) + random.choice(string.punctuation)


def ransom(text: str) -> str:
    """Randomly choose an upper or lowercase letter to return"""
    modified_text: List[str] = []
    for char in text:
        if random.choice([0, 1]):
            modified_text.append(char.upper())
        else:
            modified_text.append(char.lower())
    return ''.join(modified_text)


def test_clean():
    assert clean('') == ''
    assert clean("states,") == 'states'
    assert clean("Don't") == 'Dont'


def test_ransom():
    state = random.getstate()
    random.seed(1)
    assert ransom('Money') == 'moNeY'
    assert ransom('Dollars') == 'DOLlaRs'
    random.setstate(state)


def test_l33t():
    state = random.getstate()
    random.seed(1)
    assert l33t('Money') == 'moNeY{'
    assert l33t('Dollars') == 'Doll4r5`'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
