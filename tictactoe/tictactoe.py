"""
Tic Tac Toe Player
"""
#Works
# https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/
# https://cs50.harvard.edu/ai/2024/notes/0/

#X is the max player!!!!!

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X # X starts
    number_of_x = sum(sublist.count(X) for sublist in board)
    number_of_o = sum(sublist.count(O) for sublist in board)

    if number_of_x == number_of_o:
        return X  # X's move
    else:
        return O  # O's move



def actions(board):
    if terminal(board):
        return {(0,0)} # Random value
    actions = set()
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                cell = (row, col)
                actions.add(cell)
    return actions


def result(board, action):
    #Shallow copy
    new_board = [row[:] for row in board]
    try:
        print(action)
        if new_board[action[0]][action[1]] == None:
            new_board[action[0]][action[1]] = player(board) 
            print(board)
            return new_board
        else:
            raise RuntimeError('Wrong Board')
    except IndexError:
        raise RuntimeError('Wrong Index!!')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError



def terminal(board):
    number_of_EMPTYS = sum(sublist.count(EMPTY) for sublist in board)
    if number_of_EMPTYS == 0:
        print('Draw')
        return True

    # Check rows
    for row in range(len(board)):
        if board[row] == ["X", "X", "X"] or board[row] == ["O", "O", "O"]:
            print('ROW')
            return True

    #Check cols
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            print('COL')
            return True
    
    #Check diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        print('D1')
        return True
    
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY: 
        print('D2')
        return True

    return False
    
    
def utility(board):
    #Can't get utility of unfinished game - just-in-case
    if not terminal(board):
        return None
    
    number_of_EMPTYS = sum(sublist.count(EMPTY) for sublist in board)
    if number_of_EMPTYS == 0:
        print('Draw')
        return 0
    
    #ROWS (X is the max player)
    for row in range(len(board)):
        if board[row] == ["X", "X", "X"]:
            return 1
        elif board[row] == ["O", "O", "O"]:
            return -1
    
    #COLS (X is the max player)
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            if board[0][col] == X:
                return 1
            elif board[0][col] == O:
                return -1
    
    #Check diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        # X is the max player
        if board[0][0] == X:
            return 1
        elif board[0][0] == O:
            return -1
    
    #Check the other diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY: 
        if board[1][1] == X:
            return 1
        elif board[1][1] == O:
            return -1


def minimax(board):
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
    
    if player(board) == X:
        move = (None, float('-inf'))
        for action in actions(board):
            v = min_value(result(board, action))
            if v > move[1]:
                move = (action, v)
    else:   
        move = (None, float('inf'))
        for action in actions(board):
            v = max_value(result(board, action))
            if v < move[1]:
                move = (action, v)
    return move[0]