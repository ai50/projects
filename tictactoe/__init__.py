import sys

import check50
import check50.py

# Players
X = "X"
O = "O"
EMPTY = None

@check50.check()
def exists():
    """tictactoe.py exists"""
    check50.exists("tictactoe.py")


@check50.check(exists)
def imports():
    """tictactoe.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("tictactoe.py")


@check50.check(imports)
def test_initial():
    """initial_state returns empty board"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    expected = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    result = tictactoe.initial_state()
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_player0():
    """player returns X for initial position"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = X
    result = tictactoe.player(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_player1():
    """player returns O after one move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, X, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = O
    result = tictactoe.player(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_player2():
    """player returns X after four moves"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, X, EMPTY], [EMPTY, O, EMPTY], [O, X, EMPTY]]
    expected = X
    result = tictactoe.player(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_player3():
    """player returns O after five moves"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, X, EMPTY], [X, O, EMPTY], [O, X, EMPTY]]
    expected = O
    result = tictactoe.player(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_actions0():
    """actions returns all actions on first move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    result = tictactoe.actions(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_actions1():
    """actions returns valid actions for second move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, EMPTY], [X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = {(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    result = tictactoe.actions(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_actions2():
    """actions returns valid actions for fifth move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, EMPTY, O], [X, EMPTY, EMPTY], [EMPTY, EMPTY, X]]
    expected = {(0, 1), (1, 1), (1, 2), (2, 0), (2, 1)}
    result = tictactoe.actions(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_result0():
    """result returns correct result on X's first move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    result = tictactoe.result(board, (0, 2))
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_result1():
    """result returns correct result on O's first move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, O], [EMPTY, EMPTY, EMPTY]]
    result = tictactoe.result(board, (1, 2))
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_result2():
    """result returns correct result on third move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, O], [EMPTY, EMPTY, EMPTY]]
    expected = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, O], [X, EMPTY, EMPTY]]
    result = tictactoe.result(board, (2, 0))
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_result_exception0():
    """result raises exception on taken move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, O], [X, EMPTY, EMPTY]]
    try:
        result = tictactoe.result(board, (2, 0))
    except Exception:
        return
    raise check50.Failure("expected exception, none caught")


@check50.check(imports)
def test_result_exception1():
    """result raises exception on out-of-bounds move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, O], [X, EMPTY, EMPTY]]
    try:
        result = tictactoe.result(board, (3, 1))
    except Exception:
        return
    raise check50.Failure("expected exception, none caught")


@check50.check(imports)
def test_result_exception2():
    """result raises exception on negative out-of-bounds move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, O], [X, EMPTY, EMPTY]]
    try:
        result = tictactoe.result(board, (-1, 2))
    except Exception:
        return
    raise check50.Failure("expected exception, none caught")


@check50.check(imports)
def test_result_unchanged():
    """result does not change the original board"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, O], [X, EMPTY, EMPTY]]
    saved = board.copy()
    result = tictactoe.result(board, (0, 0))
    if board != saved:
        raise check50.Failure("original board modified")


@check50.check(imports)
def test_winner0():
    """winner finds no winner on initial board"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = None
    result = tictactoe.winner(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_winner1():
    """winner finds winner when X wins horizontally"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, O, EMPTY], [EMPTY, EMPTY, EMPTY], [X, X, X]]
    expected = X
    result = tictactoe.winner(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))

@check50.check(imports)
def test_winner2():
    """winner finds winner when O wins vertically"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, O, EMPTY], [EMPTY, O, X], [X, O, X]]
    expected = O
    result = tictactoe.winner(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_winner3():
    """winner finds winner when X wins diagonally"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, X, X], [EMPTY, X, EMPTY], [X, O, O]]
    expected = X
    result = tictactoe.winner(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_winner4():
    """winner finds no winner in tied game"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, X, X], [X, X, O], [O, O, X]]
    expected = None
    result = tictactoe.winner(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_terminal0():
    """terminal returns True in tied game"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, X, X], [X, X, O], [O, O, X]]
    expected = True
    result = tictactoe.terminal(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_terminal1():
    """terminal returns False in initial state"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = False
    result = tictactoe.terminal(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_terminal2():
    """terminal returns True if X has won the game"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, O, O], [X, X, X], [EMPTY, EMPTY, EMPTY]]
    expected = True
    result = tictactoe.terminal(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_terminal3():
    """terminal returns False in middle of game"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, O, O], [EMPTY, X, X], [EMPTY, O, X]]
    expected = False
    result = tictactoe.terminal(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_utility0():
    """utility returns 0 in tied game"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, X, X], [X, X, O], [O, O, X]]
    expected = 0
    result = tictactoe.utility(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_utility1():
    """utility returns 1 when X wins"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[X, O, O], [EMPTY, X, EMPTY], [EMPTY, EMPTY, X]]
    expected = 1
    result = tictactoe.utility(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_minimax0():
    """minimax blocks immediate three-in-a-row threat"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, X, O], [EMPTY, X, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = (2, 1)
    result = tictactoe.minimax(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_minimax1():
    """minimax finds only winning move"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[EMPTY, EMPTY, EMPTY], [X, O, O], [EMPTY, X, EMPTY]]
    expected = (2, 0)
    result = tictactoe.minimax(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_minimax2():
    """minimax finds best move near end of game"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, X, O], [X, X, EMPTY], [X, O, EMPTY]]
    expected = (1, 2)
    result = tictactoe.minimax(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_minimax_none0():
    """minimax returns None in tied game"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[O, X, O], [X, X, O], [X, O, X]]
    expected = None
    result = tictactoe.minimax(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_minimax_none1():
    """minimax returns None after X wins"""
    sys.path = [""] + sys.path
    tictactoe = check50.py.import_("tictactoe.py")
    board = [[X, X, X], [O, O, EMPTY], [EMPTY, EMPTY, EMPTY]]
    expected = None
    result = tictactoe.minimax(board)
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))
