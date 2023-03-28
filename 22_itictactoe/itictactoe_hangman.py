#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-06-08
Purpose: Tic-Tac-Toe
"""

# --------------------------------------------------
import random
from typing import List, Optional
from dataclasses import dataclass

# Getting the words from a file and creating a list.
f = open('../inputs/words.txt', 'r')
words = f.read()
words_list: List[str] = words.split()
f.close()


@dataclass
class State:
    word: str
    quit: bool
    winner: Optional[str]


# --------------------------------------------------
def main(chosen_word=random.choice(words_list)) -> None:
    """Make a jazz noise here"""

    state = State(word='_' * len(chosen_word),
                  quit=False,
                  winner=None)

    while True:
        print("\033[H\033[J")
        print(format_word(state.word))
        # Else, congratulate the user for winning.
        if state.winner:
            print('Game Over!')
            break
        elif state.quit:
            print('You lose, loser!')
            break
        state = get_move(state=state, chosen_word=chosen_word)


def get_move(state: State, chosen_word: str) -> State:
    """Get the player's move"""

    # The user then inputs a guess.
    if '_' not in state.word:
        state.winner = 'player'
        return state

    letter = input(f'What is your letter ? [quit to quit]: ')

    if letter == 'quit':
        state.quit = True
        return state

    word = find_letter_in_word(word=state.word, chosen_word=chosen_word, letter=letter)

    return State(word=word,
                 quit=False,
                 winner=None)


def format_word(word: str) -> str:
    """Format the board"""
    letters = []
    for letter in word:
        letters.append(letter)

    return ''.join(letters)


def find_letter_in_word(word: str, chosen_word: str, letter: str) -> str:
    # The program then checks where the letter appears in the word.
    for i in range(0, len(word)):
        # If it appears, it puts  the letter in the correct positions.
        if chosen_word[i] == letter:
            word = word[:i] + letter + word[i + 1:]

    return word


def test_find_in_letter():
    assert find_letter_in_word(word='_____', chosen_word='altar', letter='a') == 'a__a_'


# --------------------------------------------------
if __name__ == '__main__':
    main()
