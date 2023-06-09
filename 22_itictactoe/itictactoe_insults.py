#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-06-08
Purpose: Tic-Tac-Toe
"""

# --------------------------------------------------
import random
import sys
from typing import List, NamedTuple, Optional
import abuse


class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    state = State()

    while True:
        print("\033[H\033[J")
        print(format_board(state.board))

        if state.error:
            print(state.error)
        elif state.winner:
            print(f'{state.winner} has won !')
        elif state.quit:
            print(abuse.main())
            break
        elif state.draw:
            print("All right, we'll call it a draw.")
            break

        state = get_move(state=state)


def get_move(state: State) -> State:
    """Get the player's move"""

    player = state.player
    cell = input(f'Player {player}, what is your move ? [q to quit]: ')

    if cell == 'q':
        return state._replace(quit=True)

    if all([cell.isdigit(), int(cell)]) not in range(1, 10):
        return state._replace(error=f'Invalid cell "{cell}", please use 1-9')

    cell_num = int(cell)
    if state.board[cell_num - 1] in 'XO':
        return state._replace(error=f'Invalid cell "{cell}" already taken')

    board = state.board
    board[cell_num - 1] = player

    return state._replace(board=board,
                          player='O' if player == 'X' else 'X',
                          winner=find_winner(board),
                          draw='.' not in board,
                          error=None)


def format_board(board: List[str]) -> str:
    """Format the board"""
    cells = []
    for i, c in enumerate(board, start=1):
        if c == '.':
            cells.append(str(i))
        else:
            cells.append(c)
    bar: str = '-------------'
    cells_template: str = '| {} | {} | {} |'
    return '\n'.join([
        bar,
        cells_template.format(*cells[:3]), bar,
        cells_template.format(*cells[3:6]), bar,
        cells_template.format(*cells[6:]), bar
    ])


def find_winner(board: List[str]) -> Optional[str]:
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player

    return None


def test_board_no_board():
    """makes default board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    assert format_board('.' * 9) == board


def test_board_with_board():
    """makes board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    assert format_board('...OXX...') == board


def test_winning():
    """test winning boards"""

    wins = ['PPP......', '...PPP...', '......PPP', 'P..P..P..',
            '.P..P..P.', '..P..P..P', 'P...P...P', '..P.P.P..']

    for player in 'XO':
        other_player = 'O' if player == 'X' else 'X'

        for board in wins:
            board = board.replace('P', player)
            dots = [i for i in range(len(board)) if board[i] == '.']
            mut = random.sample(dots, k=2)
            test_board: str = ''
            test_board = ''.join([
                other_player if i in mut else board[i]
                for i in range(len(board))
            ])
            assert find_winner(test_board) == player


def test_losing():
    """test losing boards"""

    losing_board = list('XXOO.....')

    for _ in range(10):
        random.shuffle(losing_board)
        assert find_winner(''.join(losing_board)) is None


# --------------------------------------------------
if __name__ == '__main__':
    main()
