#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-05-04
Purpose: Make rhyming "words"
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    parser.add_argument('-dict',
                        '--dictionary',
                        metavar='dictionary',
                        help='The dictionary where words are',
                        type=argparse.FileType('rt'),
                        default='words.txt')

    return parser.parse_args()


# --------------------------------------------------
def look_in_dict(word: str, dictionary):
    """Return the word if it's in the dictionary"""
    word = word.lower()
    if word not in dictionary:
        return f'{word} is not in dictionary'
    return f'{word}'


def main():
    """Make a jazz noise here"""

    args = get_args()
    word: str = args.word
    dictionary = args.dictionary.read().rstrip()
    print_word = look_in_dict(word, dictionary)
    print(print_word)


# def test_look_in_dict():
#     """Test stemmer"""
#     assert stemmer('') == ('', '')
#     assert stemmer('cake') == ('c', 'ake')
#     assert stemmer('chair') == ('ch', 'air')
#     assert stemmer('APPLE') == ('', 'apple')
#     assert stemmer('RDNZL') == ('rdnzl', '')
#     assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
