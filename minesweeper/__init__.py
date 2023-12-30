import sys

import check50
import check50.py

@check50.check()
def exists():
    """minesweeper.py exists"""
    check50.exists("minesweeper.py")


@check50.check(exists)
def imports():
    """minesweeper.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("minesweeper.py")


@check50.check(imports)
def test_sentence_knownmines0():
    """Sentence.known_mines returns mines when conclusions possible"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3)], 2)
    expected = {(0, 1), (2, 3)}
    result = s.known_mines()
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_sentence_knownmines1():
    """Sentence.known_mines returns no mines when no conclusion possible"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3)], 1)
    expected = set()
    result = s.known_mines()
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_sentence_knownsafes0():
    """Sentence.known_safes returns mines when conclusion possible"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3)], 0)
    expected = {(0, 1), (2, 3)}
    result = s.known_safes()
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_sentence_knownsafes1():
    """Sentence.known_safes returns no mines when no conclusion possible"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3)], 1)
    expected = set()
    result = s.known_safes()
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_markmine0():
    """Sentence.mark_mine marks mine when cell in sentence"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3), (4, 5), (6, 7)], 3)
    s.mark_mine((2, 3))
    expected = {(0, 1), (4, 5), (6, 7)}
    result = s.cells
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))
    expected = 2
    result = s.count
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_markmine1():
    """Sentence.mark_mine does not mark mine when cell not in sentence"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3), (4, 5), (6, 7)], 3)
    s.mark_mine((2, 5))
    expected = {(0, 1), (2, 3), (4, 5), (6, 7)}
    result = s.cells
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))
    expected = 3
    result = s.count
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_marksafe0():
    """Sentence.mark_safe marks safe when cell in sentence"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3), (4, 5), (6, 7)], 3)
    s.mark_safe((2, 3))
    expected = {(0, 1), (4, 5), (6, 7)}
    result = s.cells
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))
    expected = 3
    result = s.count
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_marksafe1():
    """Sentence.mark_safe does not mark safe when cell not in sentence"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    s = ms.Sentence([(0, 1), (2, 3), (4, 5), (6, 7)], 3)
    s.mark_safe((2, 5))
    expected = {(0, 1), (2, 3), (4, 5), (6, 7)}
    result = s.cells
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))
    expected = 3
    result = s.count
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_addknowledge0():
    """MinesweeperAI.add_knowledge marks cell as a move made"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((0, 0), 2)
    expected = {(0, 0)}
    result = ai.moves_made
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_addknowledge1():
    """MinesweeperAI.add_knowledge marks cell as safe"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((3, 0), 2)
    expected = {(3, 0)}
    result = ai.safes
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_addknowledge2():
    """MinesweeperAI.add_knowledge adds sentence in middle of board"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((1, 1), 2)
    s = ms.Sentence({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}, 2)
    if s not in ai.knowledge:
        raise check50.Failure(f"did not find sentence {s}")


@check50.check(imports)
def test_addknowledge3():
    """MinesweeperAI.add_knowledge adds sentence in corner of board"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((3, 4), 1)
    s = ms.Sentence({(2, 3), (2, 4), (3, 3)}, 1)
    if s not in ai.knowledge:
        raise check50.Failure(f"did not find sentence {s}")


@check50.check(imports)
def test_addknowledge4():
    """MinesweeperAI.add_knowledge ignores known mines when adding new sentence"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((0, 0), 3)
    ai.mines.update({(0, 1), (1, 0), (1, 1)}) # just in case submission doesn't infer already
    ai.add_knowledge((0, 2), 3)
    s = ms.Sentence({(0, 3), (1, 2), (1, 3)}, 1)
    if s not in ai.knowledge:
        raise check50.Failure(f"did not find sentence {s}")


@check50.check(imports)
def test_addknowledge5():
    """MinesweeperAI.add_knowledge ignores known safes when adding new sentence"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((0, 0), 0)
    ai.safes.update({(0, 1), (1, 0), (1, 1)}) # just in case submission doesn't infer already
    ai.add_knowledge((0, 2), 2)
    s = ms.Sentence({(0, 3), (1, 2), (1, 3)}, 2)
    if s not in ai.knowledge:
        raise check50.Failure(f"did not find sentence {s}")


@check50.check(imports)
def test_addknowledge6():
    """MinesweeperAI.add_knowledge infers additional safe cells"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((0, 0), 0)
    expected = {(0, 0), (0, 1), (1, 0), (1, 1)}
    result = ai.safes
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_addknowledge7():
    """MinesweeperAI.add_knowledge can infer mine when given new information"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((2, 4), 1)
    ai.add_knowledge((2, 3), 1)
    ai.add_knowledge((1, 4), 0)
    ai.add_knowledge((3, 2), 0)
    expected = {(3, 4)}
    result = ai.mines
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_addknowledge8():
    """MinesweeperAI.add_knowledge can infer multiple mines when given new information"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((2, 0), 2)
    ai.add_knowledge((3, 1), 0)
    expected = {(1, 0), (1, 1)}
    result = ai.mines
    if expected != result:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def test_addknowledge9():
    """MinesweeperAI.add_knowledge can infer safe cells when given new information"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((0, 1), 1)
    ai.add_knowledge((1, 0), 1)
    ai.add_knowledge((1, 2), 1)
    ai.add_knowledge((3, 1), 0)
    ai.add_knowledge((0, 4), 0)
    ai.add_knowledge((3, 4), 0)
    safes = [(0, 0), (0, 2)]
    for safe in safes:
        if safe not in ai.safes:
            raise check50.Failure(f"did not find {safe} in safe cells when possible to conclude safe")


@check50.check(imports)
def test_addknowledge10():
    """MinesweeperAI.add_knowledge combines multiple sentences to draw conclusions"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=4, width=5)
    ai.add_knowledge((3, 0), 2)
    ai.add_knowledge((2, 0), 3)
    ai.add_knowledge((1, 2), 1)
    mines = [(1, 0), (2, 1), (3, 1)]
    for mine in mines:
        if mine not in ai.mines:
            raise check50.Failure(f"did not find {mine} in mines when possible to conclude mine")


@check50.check(imports)
def test_safemove0():
    """MinesweeperAI.make_safe_move makes safe move when possible"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=3, width=3)
    ai.add_knowledge((0, 2), 0)
    options = [(0, 1), (1, 1), (1, 2)]
    move = ai.make_safe_move()
    if move not in options:
        raise check50.Failure(f"move made not one of the safe options")


@check50.check(imports)
def test_safemove1():
    """MinesweeperAI.make_safe_move avoids cells already chosen"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=2, width=2)
    ai.add_knowledge((0, 0), 1)
    move = ai.make_safe_move()
    if move == (0, 0):
        raise check50.Failure(f"move made was one already chosen")


@check50.check(imports)
def test_safemove2():
    """MinesweeperAI.make_safe_move returns None when no safe moves available"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=3, width=3)
    ai.add_knowledge((0, 0), 1)
    move = ai.make_safe_move()
    if move is not None:
        raise check50.Failure(f"expected None when no safe move available")


@check50.check(imports)
def test_randommove0():
    """MinesweeperAI.make_random_move avoids cells that are already chosen or mines"""
    sys.path = [""] + sys.path
    ms = check50.py.import_("minesweeper.py")
    ai = ms.MinesweeperAI(height=3, width=3)
    ai.add_knowledge((0, 0), 3)
    forbidden = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for i in range(50):
        move = ai.make_random_move()
        if move in forbidden:
            raise check50.Failure(f"AI made forbidden move")


