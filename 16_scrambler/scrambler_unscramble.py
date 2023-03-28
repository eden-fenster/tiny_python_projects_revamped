#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-12
Purpose: Scramble the letters of words
"""

import argparse

# --------------------------------------------------
import os
import random
import re
from typing import List, Dict, TextIO


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-f',
                        '--file',
                        help='words file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='words.txt')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def scramble(word: str) -> str:
    """For words over 3 characters, shuffle the letters in the middle"""

    if len(word) <= 3:
        return word

    regex_word = re.match(r'\w+', word)
    if regex_word:
        middle: List[str] = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]

    return word


def split_file_into_words(file) -> List[str]:
    """Splits file into words"""
    words: List[str] = []

    for line in file.readlines():
        line = line.rstrip()
        new_words: List[str] = line.split()
        words.extend(new_words)
    return words


def create_signature(word: str) -> str:
    """Creates signature for words"""
    if len(word) <= 3:
        return word

    middle: List[str] = list(word[1:-1])
    middle.sort()
    signature: str = word[0] + ''.join(middle) + word[-1]

    return signature


def create_signature_dictionary(file: TextIO) -> Dict[str, List[str]]:
    signature_dictionary: Dict[str, List[str]] = {}
    # Read each word from dictionary file
    dictionary_list: List[str] = split_file_into_words(file=file)

    # Create signature for word
    for word in dictionary_list:
        # Add word to key of signature value.
        signature = create_signature(word)
        if signature in signature_dictionary:
            #    If it exists, just add to value list
            signature_dictionary[signature].append(word)
            continue
        #    Otherwise, create value with initial content.
        signature_dictionary[signature] = [word]

    # Return dictionary
    return signature_dictionary


# "safht" : ["shaft"]
def unscramble(word: str, signature_dictionary: Dict[str, List[str]]) -> str:
    signature = create_signature(word=word)
    result: List[str] = signature_dictionary.get(signature, [f"{word}-Unknown"])
    return result[0]


def main():
    """Make a jazz noise here"""

    args = get_args()
    text: str = args.text
    file = args.file
    seed: int = args.seed

    random.seed(seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    # Get dictionary
    dictionary = create_signature_dictionary(file=file)
    # Get lines from text
    for line in text.splitlines():
        line = line.strip()
        words: List[str] = []

        # Get words from the current line
        split_line: List[str] = splitter.split(line)
        for word in split_line:
            word = word.strip()
            if not word:
                continue
            # Unscramble each word
            unscrambled_word = unscramble(word, dictionary)
            words.append(unscrambled_word)
        # Print out unscrambled line words
        print(' '.join(words))


def test_unscramble():
    """Test unscramble"""
    state = random.getstate()
    random.seed(1)
    dictionary = create_signature_dictionary(open('words.txt', 'rt'))
    assert unscramble("a", dictionary) == "a"
    assert unscramble("ab", dictionary) == "ab-Unknown"
    assert unscramble("abc", dictionary) == "abc-Unknown"
    assert unscramble("abcd", dictionary) == "abcd-Unknown"
    assert unscramble("abcde", dictionary) == "abcde-Unknown"
    assert unscramble("abcdef", dictionary) == "abcdef-Unknown"
    assert unscramble("abcde'f", dictionary) == "abcde'f-Unknown"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
