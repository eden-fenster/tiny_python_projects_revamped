#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-04-24
Purpose: Telephone
"""

import argparse
import os

# --------------------------------------------------
import random
import string


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def replace_word(old_word: list) -> str:
    index_to_replace = random.randint(0, len(old_word) - 1)
    potential_new_characters = string.ascii_letters + string.punctuation
    new_character_index = random.randint(0, len(potential_new_characters)-1)
    new_character = potential_new_characters[new_character_index]
    prefix = old_word[:index_to_replace]
    suffix = old_word[index_to_replace + 1:]
    new_word = prefix + new_character + suffix
    return new_word

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seed: int = args.seed
    our_text: str = args.text
    mutations: float = args.mutations

    text_to_print = mutate_text(our_text, mutations, seed)

    # Output new text
    print(text_to_print)


def mutate_text(our_text, mutations, seed):
    random.seed(seed)
    # Split text into words
    our_words: list = our_text.split()
    mutation_num: int = round(mutations * len(our_words))
    print(f"We are performing {mutation_num} mutations")
    for mutation_count in range(0, mutation_num):
        # Choose random word
        word_index_to_replace: int = random.randint(0, len(our_words) - 1)
        print(f'Index {word_index_to_replace}')
        chosen_word = our_words[word_index_to_replace]

        # Modify chosen random word
        new_word = replace_word(chosen_word)

        # Put in modified word
        our_words[word_index_to_replace] = new_word
    # Combine words back into text
    new_text = ' '.join(our_words)
    return new_text


def test_replace_word():
    text = "Simple text Simple text Simple text"
    expected_response = "Simple Gext Simple text Simple text"
    response = mutate_text(our_text=text,
                           mutations=0.1,
                           seed=1)
    assert expected_response == response


# --------------------------------------------------
if __name__ == '__main__':
    main()
