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
    parser.add_argument('-a',
                        '--ac',
                        help='Add characters',
                        action='store_true',
                        default=False)
    parser.add_argument('-d',
                        '--dc',
                        help='Delete characters',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def delete_character_in_word(old_word: str) -> str:
    index_to_delete = random.randint(0, len(old_word) - 1)
    prefix = old_word[:index_to_delete]
    suffix = old_word[index_to_delete + 1:]
    new_word = prefix + suffix
    return new_word


def add_character_in_word(old_word: str) -> str:
    index_to_add = random.randint(0, len(old_word))
    potential_new_characters = string.ascii_letters + string.punctuation
    new_character_index = random.randint(0, len(potential_new_characters))
    new_character = potential_new_characters[new_character_index]
    prefix = old_word[:index_to_add]
    suffix = old_word[index_to_add:]
    new_word = prefix + new_character + suffix
    return new_word


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seed: int = args.seed
    should_add_characters: bool = args.ac
    should_delete_characters: bool = args.dc
    our_text: str = args.text
    mutation_percent: float = args.mutations

    new_text = mutate_text(our_text=our_text, mutation_percent=mutation_percent,
                           should_add_characters=should_add_characters,
                           should_delete_characters=should_delete_characters, seed=seed)

    print(f'You said: "{our_text}"\nI heard : "{new_text}"')


def mutate_text(our_text: str, mutation_percent: float, should_add_characters: bool,
                should_delete_characters: bool, seed: int):
    random.seed(seed)
    len_text: int = len(our_text)
    mutation_num: int = round(mutation_percent * len_text)
    letters_and_punctuations: str = string.ascii_letters + string.punctuation
    our_words: list = our_text.split()
    number_of_words_to_mutate: int = round(mutation_percent * len(our_words))

    if should_add_characters:
        for word_index_to_add, chosen_word in enumerate(our_words):
            random_choice = random.random()
            if mutation_percent < random_choice:
                continue

            # Modify chosen random word
            new_word = add_character_in_word(chosen_word)

            # Put in modified word
            our_words[word_index_to_add] = new_word
    if should_delete_characters:
        for word_index_to_delete, chosen_word in enumerate(our_words):
            random_choice = random.random()
            print(f"index={word_index_to_delete} rand={random_choice}, mutp={mutation_percent}")
            if mutation_percent < random_choice:
                continue

            # Modify chosen random word
            new_word = delete_character_in_word(chosen_word)

            # Put in modified word
            our_words[word_index_to_delete] = new_word

    # Combine words back into text
    new_text: str = ' '.join(our_words)

    for random_index in random.sample(range(len_text), mutation_num):
        new_char = random.choice(letters_and_punctuations.replace(new_text[random_index], ''))
        new_text = new_text[:random_index] + new_char + new_text[random_index + 1:]
    return new_text

# def test_mutate_text():
#     """Test mutate_text"""




# --------------------------------------------------
if __name__ == '__main__':
    main()

def test_no_change():
    text = "Simple text"
    response = mutate_text(
        our_text=text,
        mutation_percent=0,
        should_delete_characters=False,
        should_add_characters=False, seed=1)
    assert text == response

def test_simple_change():
    text = "Simple text"
    expected_response = "Si@ple text"
    response = mutate_text(
        our_text=text,
        mutation_percent=1/len(text),
        should_delete_characters=False,
        should_add_characters=False, seed=1)
    assert expected_response == response

def test_add_character():
    text = "Simple text Simple text Simple text Simple Simple text"
    expected_response = "nimple text Simple text Sim'le text SiJple SimplE\\Xtext"
    response = mutate_text(
        our_text=text,
        mutation_percent=0.1,
        should_delete_characters=False,
        should_add_characters=True, seed=1)
    assert expected_response == response

def test_delete_character():
    text = "Simple text Simple text Simple text Simple text Simple Text"
    expected_response = "Oimple text Simple text 'imJle text SiEple text ]ople Text"
    response = mutate_text(
        our_text=text,
        mutation_percent=0.1,
        should_delete_characters=True,
        should_add_characters=False, seed=1)
    assert expected_response == response