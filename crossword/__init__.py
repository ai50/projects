import copy
import sys

import check50
import check50.py


def get_domains(domains):
    result = dict()
    for v in domains:
        result[v.i, v.j, v.direction] = domains[v]
    return result


@check50.check()
def exists():
    """generate.py exists"""
    check50.include("crossword.py")
    check50.include("data")
    check50.exists("generate.py")


@check50.check(exists)
def imports():
    """generate.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("generate.py")


@check50.check(imports)
def enforce_node_consistency():
    """enforce_node_consistency removes node inconsistent domain values"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words0.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.enforce_node_consistency()

    # Test
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY"},
        Var(0, 2, "down", 3): {"ODE"},
        Var(2, 1, "across", 5): {"TODAY", "READY"}
    }
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def enforce_node_consistency2():
    """enforce_node_consistency removes multiple node inconsistent domain values"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words1.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.enforce_node_consistency()

    # Test
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def revise0():
    """revise does nothing when no revisions possible"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words0.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY"},
        Var(0, 2, "down", 3): {"ODE"},
        Var(2, 1, "across", 5): {"TODAY", "READY"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY"},
        Var(0, 2, "down", 3): {"ODE"},
        Var(2, 1, "across", 5): {"TODAY", "READY"}
    }
    creator.revise(Var(0, 2, "down", 3), Var(0, 1, "across", 5))
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def revise1():
    """revise removes value from domain when revision is possible"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words1.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    creator.revise(Var(0, 1, "across", 5), Var(0, 2, "down", 3))
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def revise2():
    """revise removes multiple values from domain when revision is possible"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words1.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"READY", "HELLO", "AMAZE"}
    }
    creator.revise(Var(2, 1, "across", 5), Var(0, 2, "down", 3))
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def ac3_0():
    """ac3 updates domains when only one possible solution"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words0.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY"},
        Var(0, 2, "down", 3): {"ODE"},
        Var(2, 1, "across", 5): {"TODAY", "READY"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY"},
        Var(0, 2, "down", 3): {"ODE"},
        Var(2, 1, "across", 5): {"READY"}
    }
    creator.ac3()
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def ac3_1():
    """ac3 updates domains when multiple possible domain values exist"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words1.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"READY", "HELLO", "AMAZE"}
    }
    creator.ac3()
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def ac3_2():
    """ac3 does nothing when given an emtpy starting list of arcs"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words1.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    creator.ac3(arcs=[])
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def ac3_3():
    """ac3 handles processing arcs when an initial list of arcs is provided"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words1.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    creator.ac3(arcs=[(Var(0, 2, "down", 3), Var(2, 1, "across", 5))])
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def ac3_3():
    """ac3 handles processing arcs when an initial list of arcs is provided"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure0.txt", "data/test_words1.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    expected = {
        Var(0, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"},
        Var(0, 2, "down", 3): {"ODE", "ELM"},
        Var(2, 1, "across", 5): {"TODAY", "READY", "HELLO", "AMAZE", "FORGE"}
    }
    creator.ac3(arcs=[(Var(0, 2, "down", 3), Var(2, 1, "across", 5))])
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def ac3_4():
    """ac3 handles multiple rounds of updates"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words2.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "SLOPE", "GRANT", "WHERE", "CLOTH"},
        Var(0, 2, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(2, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "SLOPE", "GRANT", "WHERE", "CLOTH"},
        Var(2, 4, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(4, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "SLOPE", "GRANT", "WHERE", "CLOTH"}
    }
    expected = {
        Var(0, 1, "across", 5): {"DAISY"},
        Var(0, 2, "down", 3): {"AIL"},
        Var(2, 1, "across", 5): {"SLOPE"},
        Var(2, 4, "down", 3): {"PAN"},
        Var(4, 1, "across", 5): {"GRANT", "FRONT"}
    }
    creator.ac3()
    for var in expected:
        if expected[var] != creator.domains[var]:
            raise check50.Mismatch(str(expected[var]), str(creator.domains[var]))


@check50.check(imports)
def ac_5():
    """ac3 returns False if no solution possible"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words3.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "GRANT", "WHERE", "CLOTH"},
        Var(0, 2, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(2, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "GRANT", "WHERE", "CLOTH"},
        Var(2, 4, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(4, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "GRANT", "WHERE", "CLOTH"}
    }
    result = creator.ac3()
    if result:
        raise check50.Mismatch(str(False), str(result))


@check50.check(imports)
def assignment_complete0():
    """assignment_complete identifies complete assignment"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words4.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    assignment = {
        Var(0, 1, "across", 5): "WHERE",
        Var(0, 2, "down", 3): "RAM",
        Var(2, 1, "across", 5): "SLOPE",
        Var(2, 4, "down", 3): "PAN",
        Var(4, 1, "across", 5): "PAINT"
    }

    result = creator.assignment_complete(assignment)
    expected = True
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def assignment_complete1():
    """assignment_complete identifies incomplete assignment"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words4.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    assignment = {
        Var(0, 1, "across", 5): "WHERE",
        Var(2, 1, "across", 5): "SLOPE",
        Var(2, 4, "down", 3): "PAN",
        Var(4, 1, "across", 5): "PAINT"
    }

    result = creator.assignment_complete(assignment)
    expected = False
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def consistent0():
    """consistent identifies consistent assignment"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words4.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    assignment = {
        Var(0, 1, "across", 5): "DAISY",
        Var(0, 2, "down", 3): "AIL",
        Var(2, 1, "across", 5): "SLOPE",
        Var(2, 4, "down", 3): "PAN",
        Var(4, 1, "across", 5): "GRANT"
    }

    result = creator.consistent(assignment)
    expected = True
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def consistent1():
    """consistent identifies when assignment doesn't meet unary constraints"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words4.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    assignment = {
        Var(0, 1, "across", 5): "RAT",
        Var(0, 2, "down", 3): "AIL",
        Var(2, 1, "across", 5): "SLOPE",
        Var(2, 4, "down", 3): "PAN",
        Var(4, 1, "across", 5): "GRANT"
    }

    result = creator.consistent(assignment)
    expected = False
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def consistent2():
    """consistent identifies when assignment doesn't meet binary constraints"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words4.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    assignment = {
        Var(0, 1, "across", 5): "DAISY",
        Var(0, 2, "down", 3): "AIL",
        Var(2, 1, "across", 5): "SLOPE",
        Var(2, 4, "down", 3): "PAN",
        Var(4, 1, "across", 5): "CLOTH"
    }

    result = creator.consistent(assignment)
    expected = False
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def consistent3():
    """consistent identifies when assignment doesn't meet uniqueness constraints"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words4.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    assignment = {
        Var(0, 1, "across", 5): "PAINT",
        Var(0, 2, "down", 3): "AIL",
        Var(2, 1, "across", 5): "SLOPE",
        Var(2, 4, "down", 3): "PAN",
        Var(4, 1, "across", 5): "PAINT"
    }

    result = creator.consistent(assignment)
    expected = False
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def consistent3():
    """consistent identifies consistent incomplete assignments"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words4.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    assignment = {
        Var(0, 1, "across", 5): "DAISY",
        Var(2, 1, "across", 5): "SLOPE",
        Var(4, 1, "across", 5): "GRANT"
    }

    result = creator.consistent(assignment)
    expected = True
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def order_domain_values0():
    """order_domain_values returns all available domain values"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure2.txt", "data/test_words5.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"HELLO", "COINS"},
        Var(0, 2, "down", 3): {"ELM", "ELK", "OAK"},
    }
    assignment = dict()
    result = set(creator.order_domain_values(Var(0, 1, "across", 5), assignment))
    expected = {"HELLO", "COINS"}
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def order_domain_values1():
    """order_domain_values returns all available domain values in correct order"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure2.txt", "data/test_words5.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"HELLO", "COINS"},
        Var(0, 2, "down", 3): {"ELM", "ELK", "OAK"},
    }
    assignment = dict()
    result = creator.order_domain_values(Var(0, 1, "across", 5), assignment)
    expected = ["HELLO", "COINS"]
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def select_unassigned_variable0():
    """select_unassigned_variable returns variable with minimum remaining values"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words3.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "GRANT", "WHERE", "CLOTH"},
        Var(0, 2, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(2, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "GRANT", "WHERE", "CLOTH"},
        Var(2, 4, "down", 3): {"RAM", "AIL", "PAN"},
        Var(4, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "GRANT", "WHERE", "CLOTH"}
    }
    assignment = dict()
    result = creator.select_unassigned_variable(assignment)
    expected = Var(2, 4, "down", 3)
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def select_unassigned_variable1():
    """select_unassigned_variable returns variable with highest degree with remaining values tied"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words2.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"SLOPE", "FRONT"},
        Var(0, 2, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(2, 1, "across", 5): {"SLOPE", "FRONT"},
        Var(2, 4, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(4, 1, "across", 5): {"FRONT", "AMAZE", "DAISY", "GRANT", "WHERE", "CLOTH"}
    }
    assignment = dict()
    result = creator.select_unassigned_variable(assignment)
    expected = Var(2, 1, "across", 5)
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def select_unassigned_variable1():
    """select_unassigned_variable doesn't choose a variable if already assigned"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words2.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    creator.domains = {
        Var(0, 1, "across", 5): {"SLOPE", "FRONT", "DAISY"},
        Var(0, 2, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(2, 1, "across", 5): {"SLOPE", "FRONT"},
        Var(2, 4, "down", 3): {"RAM", "AIL", "PAN", "RAT"},
        Var(4, 1, "across", 5): {"GRANT"}
    }
    assignment = {
        Var(4, 1, "across", 5): {"GRANT"}
    }
    result = creator.select_unassigned_variable(assignment)
    expected = Var(2, 1, "across", 5)
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def backtrack0():
    """backtrack returns assignment if possible to calculate"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words6.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    result = creator.solve()
    expected = {
        Var(0, 1, "across", 5): "DAISY",
        Var(0, 2, "down", 3): "AIL",
        Var(2, 1, "across", 5): "SLOPE",
        Var(2, 4, "down", 3): "PAN",
        Var(4, 1, "across", 5): "FRONT"
    }
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))


@check50.check(imports)
def backtrack1():
    """backtrack returns no assignment if not possible to calculate"""

    # Setup
    sys.path = [""] + sys.path
    generate = check50.py.import_("generate.py")
    Var = generate.Variable
    crossword = generate.Crossword("data/test_structure1.txt", "data/test_words3.txt")
    creator = generate.CrosswordCreator(crossword)

    # Action
    result = creator.solve()
    expected = None
    if result != expected:
        raise check50.Mismatch(str(expected), str(result))
