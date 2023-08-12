"""
Tic Tac Toe Player
"""

import math
import copy


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
    countX = 0
    countO = 0
    empty = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                if board[i][j] == X:
                    countX += 1
                else:
                    countO += 1
                empty = False
    if empty or countO == countX:
       # print("it is player X turn")
        return X 
    else:
       # print("it is player O turn")
        return O  
    

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x = action[0]
    y = action[1]
    if board[x][y] != EMPTY:
        # print("not empty cell")
        raise Exception("not empty cell")
    if x > 2 or y > 2 or x < 0 or y < 0 :
        # print("cell outside borders")
        raise Exception("cell outside borders")
    board2 = copy.deepcopy(board)
    board2[action[0]][action[1]] = player(board)
    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check row
    for i in range(len(board)):
        s  = set(board[i])
        
        if len(s) == 1 and board[i][0] != EMPTY:
            # print("row winner found set = ", board[i])
            return board[i][0]
    
    copy = board
    transposed = [[copy[j][i] for j in range(len(copy))]for i in range(len(copy[0]))]
    # print("transposed ", transposed)
    # check columns
    for i in range(len(transposed)):
        s  = set(transposed[i])
        if len(s) == 1 and transposed[i][0] != EMPTY:
            # print("column winner found set = ", transposed[i])
            return transposed[i][0]
    
    #check diagonals
    s = set()
    for i in range(len(board)):
        s.add(board[i][i])

    if len(s) == 1 and board[0][0] != EMPTY: 
        # print("main diagonal winner found set = ", s)
        return board[0][0]

    s = set()
    for i in range(len(board)):
        s.add(board[i][len(board) - i - 1])
    if len(s) == 1 and board[0][len(board)-1] != EMPTY: 
        # print("second diagonal winner found set = ", s)
        return board[0][len(board)-1]

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win == None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == EMPTY:
                    return False
    return True                
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     playerTurn = player(board)
#     #player X
#     if playerTurn == X:
#         v = max(board)
#         return(v[1], v[2])
#     #player O
#     else:
#         v = min(board)
#         return(v[1], v[2])

# def max(board):
#         possibleActions = actions(board)
#         u = utility(board)
#         if u == 1:
#             return (1, -2, -2)
#         elif u == -1:
#             return (-1, -2, -2)
#         if (len(possibleActions)) == 0:
#             return (0, -2, -2)

#         maxValue = -math.inf
#         dx = None
#         dy = None
     
#         for action in possibleActions:
#             i = action[0]
#             j = action[1]
#             newBoard = result(board, (i,j))
#             (v, _, _) = min(newBoard)
#             if v > maxValue:
#                 maxValue = v
#                 dx = i
#                 dy = j
#         return (maxValue, dx, dy)    

# def min(board):
#         possibleActions = actions(board)
#         u = utility(board)
#         if u == 1:
#             return (1, -2, -2)
#         elif u == -1:
#             return (-1, -2, -2)
#         if (len(possibleActions)) == 0:
#             return (0, -2, -2)
#         minValue = math.inf
#         dx = None
#         dy = None
     
#         for action in possibleActions:
#             i = action[0]
#             j = action[1]
#             newBoard = result(board, (i,j))
#             (v, _, _) = max(newBoard)
#             if v < minValue:
#                 minValue = v
#                 dx = i
#                 dy = j
#         return (minValue, dx, dy)    

# Alpha-Beta prunning
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    playerTurn = player(board)
    #player X
    if playerTurn == X:
        v = max_alpha_beta(board, -math.inf, math.inf)
        return(v[1], v[2])
    #player O
    else:
        v = min_alpha_beta(board, -math.inf, math.inf)
        return(v[1], v[2])

def max_alpha_beta(board, alpha, beta):
        possibleActions = actions(board)
        u = utility(board)
        if u == 1:
            return (1, -2, -2)
        elif u == -1:
            return (-1, -2, -2)
        if (len(possibleActions)) == 0:
            return (0, -2, -2)

        maxValue = -math.inf
        dx = None
        dy = None
     
        for action in possibleActions:
            i = action[0]
            j = action[1]
            newBoard = result(board, (i,j))
            (v, _, _) = min_alpha_beta(newBoard, alpha, beta)
            if v > maxValue:
                maxValue = v
                dx = i
                dy = j
            # best max value up till now is bigger than beta
            # no need to continue to next branch = prunning
            if maxValue >= beta:
                return(maxValue, dx, dy)
            # update alpha if necessary
            if alpha < maxValue:
                alpha = maxValue
        return (maxValue, dx, dy)    

def min_alpha_beta(board, alpha, beta):
        possibleActions = actions(board)
        u = utility(board)
        if u == 1:
            return (1, -2, -2)
        elif u == -1:
            return (-1, -2, -2)
        if (len(possibleActions)) == 0:
            return (0, -2, -2)
        minValue = math.inf
        dx = None
        dy = None
     
        for action in possibleActions:
            i = action[0]
            j = action[1]
            newBoard = result(board, (i,j))
            (v, _, _) = max_alpha_beta(newBoard, alpha, beta)
            if v < minValue:
                minValue = v
                dx = i
                dy = j
            # best min value up till now is smaller than alpha
            # no need to continue to next branch = prunning
            if minValue <= alpha:
                return(minValue, dx, dy)
            # update beta if necessary
            if minValue < beta:
                beta = minValue
        return (minValue, dx, dy)
            
