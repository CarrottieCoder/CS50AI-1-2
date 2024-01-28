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


def result(board, action):
    #Shallow copy
    new_board = [row[:] for row in board]
    try:
        #TypeError: 'NoneType' object is not subscriptable
        if new_board[action[0]][action[1]] == None:
            new_board[action[0]][action[1]] = player(board) 
            print(board)
            return new_board
        else:
            print(new_board[action[0]][action[1]])
            raise RuntimeError('Wrong Board')
    except IndexError:
        print('Wrong Index')
        raise RuntimeError('Wrong Index!!')
    
    
    
print(result([[EMPTY, EMPTY, EMPTY],
            [EMPTY, "X", EMPTY],
            [EMPTY, EMPTY, EMPTY]], (0,0)))