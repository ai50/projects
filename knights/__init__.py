import sys

import check50
import check50.py

@check50.check()
def exists():
    """puzzle.py exists"""
    check50.include("logic.py")
    check50.exists("puzzle.py")


@check50.check(exists)
def imports():
    """puzzle.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("puzzle.py")


@check50.check(imports)
def test_puzzle0():
    """knowledge0 solves Puzzle 0"""
    sys.path = [""] + sys.path
    puzzle = check50.py.import_("puzzle.py")
    knowledge = puzzle.knowledge0
    trues = [puzzle.AKnave]
    falses = [puzzle.AKnight, puzzle.BKnight, puzzle.BKnave, puzzle.CKnight, puzzle.CKnave]
    for true in trues:
        if not puzzle.model_check(knowledge, true):
            raise check50.Failure(f"failed to infer {true}")
    for false in falses:
        if puzzle.model_check(knowledge, false):
            raise check50.Failure("incorrectly inferred {false}")


@check50.check(imports)
def test_puzzle1():
    """knowledge1 solves Puzzle 1"""
    sys.path = [""] + sys.path
    puzzle = check50.py.import_("puzzle.py")
    knowledge = puzzle.knowledge1
    trues = [puzzle.AKnave, puzzle.BKnight]
    falses = [puzzle.AKnight, puzzle.BKnave, puzzle.CKnight, puzzle.CKnave]
    for true in trues:
        if not puzzle.model_check(knowledge, true):
            raise check50.Failure(f"failed to infer {true}")
    for false in falses:
        if puzzle.model_check(knowledge, false):
            raise check50.Failure("incorrectly inferred {false}")


@check50.check(imports)
def test_puzzle2():
    """knowledge2 solves Puzzle 2"""
    sys.path = [""] + sys.path
    puzzle = check50.py.import_("puzzle.py")
    knowledge = puzzle.knowledge2
    trues = [puzzle.AKnave, puzzle.BKnight]
    falses = [puzzle.AKnight, puzzle.BKnave, puzzle.CKnight, puzzle.CKnave]
    for true in trues:
        if not puzzle.model_check(knowledge, true):
            raise check50.Failure(f"failed to infer {true}")
    for false in falses:
        if puzzle.model_check(knowledge, false):
            raise check50.Failure("incorrectly inferred {false}")


@check50.check(imports)
def test_puzzle3():
    """knowledge3 solves Puzzle 3"""
    sys.path = [""] + sys.path
    puzzle = check50.py.import_("puzzle.py")
    knowledge = puzzle.knowledge3
    trues = [puzzle.AKnight, puzzle.BKnave, puzzle.CKnight]
    falses = [puzzle.AKnave, puzzle.BKnight, puzzle.CKnave]
    for true in trues:
        if not puzzle.model_check(knowledge, true):
            raise check50.Failure(f"failed to infer {true}")
    for false in falses:
        if puzzle.model_check(knowledge, false):
            raise check50.Failure("incorrectly inferred {false}")


@check50.check(imports)
def test_no_answers_given():
    """knowledge bases do not explicitly encode solutions directly"""
    sys.path = [""] + sys.path
    puzzle = check50.py.import_("puzzle.py")
    solutions = [
        (puzzle.knowledge0, [puzzle.AKnave]),
        (puzzle.knowledge1, [puzzle.AKnave, puzzle.BKnight]),
        (puzzle.knowledge2, [puzzle.AKnave, puzzle.BKnight]),
        (puzzle.knowledge3, [puzzle.AKnight, puzzle.BKnave, puzzle.CKnight])
    ]
    for knowledge, symbols in solutions:
        for symbol in symbols:
            if symbol in knowledge.conjuncts:
                raise check50.Failure(f"found {symbol} explicitly encoded")
