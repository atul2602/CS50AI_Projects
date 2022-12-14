"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    countX=0
    countO=0

    for row in board:
        for element in row:
            if element==X:
                countX+=1
            elif element==O:
                countO+=1

    if(countX>countO): return O
    elif(countO>countX): return X
    else: return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    output = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                output.add((i,j))

    return output

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]

    if(board[row][col] != EMPTY): raise ValueError("Action not valid.")

    new_board=deepcopy(board)
    new_board[row][col]=player(board)

    return new_board

def diag1_winner(board):
    mark = board[0][0]
    if mark == board[1][1] == board[2][2]:
        return mark
    
    else:
        return None

def diag2_winner(board):
    mark = board[0][2]

    if mark == board[1][1] == board[2][0]:
        return mark

    else:
        return None

def col_winner(board):
    for j in range(3):
        mark = board[0][j]
        res = True
        for i in range(3):
            if(mark != board[i][j]):
                res = False
        if res:
            return mark

    return None

def row_winner(board):
    for i in range(3):
        mark=board[i][0]
        res = True
        for j in range(3):
            if(mark!=board[i][j]):
                res = False
                break
        if res:
            return mark

    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if diag1_winner(board) is not None:
        return(diag1_winner(board))

    elif diag2_winner(board) is not None:
        return(diag2_winner(board))

    elif col_winner(board) is not None:
        return col_winner(board)

    else:
        return row_winner(board)

def filled(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return filled(board) or (winner(board) is not None)
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_ = winner(board)

    if winner_ == X:
        return 1

    elif winner_ == O:
        return -1

    else:
        return 0

def max_value(board):
    actions_ = actions(board)

    if terminal(board):
        return utility(board), None
    else:
        v=-math.inf
        max_play = None
        for action in actions_:
            temp = min_value(result(board, action))[0]
            if temp > v:
                max_play = action
                v = temp
        
        return v, max_play

def min_value(board):
    """
    Returns the best possible scenario for min player O
    """
    actions_ = actions(board)

    if terminal(board):
        return utility(board), None
    else:
        v=math.inf
        min_play = None
        for action in actions_:
            temp = max_value(result(board, action))[0]
            if temp < v:
                min_play = action
                v = temp
        
        return v, min_play

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    player_ = player(board)
    if terminal(board):
        return None

    if player_ == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]

    




