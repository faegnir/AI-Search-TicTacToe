"""
Tic Tac Toe Player
"""

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
    """Returns player who has the next turn on a board."""
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O
        

def actions(board):
    """Returns set of all possible actions (i, j) available on the board."""
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """Returns the board that results from making move (i, j) on the board."""
    i, j = action
    if board[i][j] != EMPTY or not (0 <= i < 3 and 0 <= j < 3):
        raise Exception("Invalid action")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board
    

def winner(board):
    """Returns the winner of the game, if there is one."""
    for player in (X, O):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return player
            if all(board[j][i] == player for j in range(3)):
                return player
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return player
    return None
        

def terminal(board):
    """Returns True if game is over, False otherwise."""
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)



def utility(board):
    """Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """Returns the optimal action for the current player on the board."""
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value = -float("inf")
        best_action = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > value:
                value = min_val
                best_action = action
    else:
        value = float("inf")
        best_action = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < value:
                value = max_val
                best_action = action

    return best_action



def max_value(board):
    if terminal(board):
        return utility(board)
    value = -float("inf")
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    value = float("inf")
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
