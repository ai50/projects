import sys

import check50
import check50.py

FAMILIES = [

    # 0: simple
    {
        "Harry": {"name": "Harry", "mother": "Lily", "father": "James", "trait": None},
        "James": {"name": "James", "mother": None, "father": None, "trait": None},
        "Lily": {"name": "Lily", "mother": None, "father": None, "trait": None}
    },

    # 1: multiple children
    {
        "Arthur": {"name": "Arthur", "mother": None, "father": None, "trait": None},
        "Charlie": {"name": "Charlie", "mother": "Molly", "father": "Arthur", "trait": None},
        "Fred": {"name": "Fred", "mother": "Molly", "father": "Arthur", "trait": None},
        "Ginny": {"name": "Ginny", "mother": "Molly", "father": "Arthur", "trait": None},
        "Molly": {"name": "Molly", "mother": None, "father": None, "trait": None},
        "Ron": {"name": "Ron", "mother": "Molly", "father": "Arthur", "trait": None}
    },

    # 2: multiple generations
    {
        "Arthur": {"name": "Arthur", "mother": None, "father": None, "trait": None},
        "Hermione": {"name": "Hermione", "mother": None, "father": None, "trait": None},
        "Molly": {"name": "Molly", "mother": None, "father": None, "trait": None},
        "Ron": {"name": "Ron", "mother": "Molly", "father": "Arthur", "trait": None},
        "Rose": {"name": "Rose", "mother": "Ron", "father": "Hermione", "trait": None}
    }
]

def assert_within(actual, expected, tolerance, name="value"):
    lower = expected - tolerance
    upper = expected + tolerance
    if not lower <= actual <= upper:
        raise check50.Failure(f"expected {name} to be in range [{lower}, {upper}], got {actual} instead")


@check50.check()
def exists():
    """heredity.py exists"""
    check50.exists("heredity.py")


@check50.check(exists)
def imports():
    """heredity.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("heredity.py")


@check50.check(imports)
def test_jp0():
    """joint_probability returns correct results for no gene or trait in simple family"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[0], set(), set(), set())
    assert_within(p, 0.8764, 0.01, "joint probability")


@check50.check(imports)
def test_jp1():
    """joint_probability returns correct results for presence of gene and trait in simple family"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[0], {"Harry"}, {"James"}, {"James"})
    assert_within(p, 0.002664, 0.0001, "joint probability")


@check50.check(imports)
def test_jp2():
    """joint_probability returns correct results for no gene or trait in family with multiple children"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[1], set(), set(), set())
    assert_within(p, 0.8006, 0.01, "joint probability")


@check50.check(imports)
def test_jp3():
    """joint_probability returns correct results for presence of trait in family with multiple children"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[1], set(), set(), {"Ginny"})
    assert_within(p, 0.008087, 0.0001, "joint probability")


@check50.check(imports)
def test_jp4():
    """joint_probability returns correct results for presence of gene in family with multiple children"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[1], {"Molly"}, set(), set())
    assert_within(p, 0.0007235, 0.00001, "joint probability")


@check50.check(imports)
def test_jp5():
    """joint_probability returns correct results for presence of gene and trait in family with multiple children"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[1], {"Arthur", "Ron"}, set(), {"Arthur"})
    assert_within(p, 0.0004133, 0.00001, "joint probability")


@check50.check(imports)
def test_jp6():
    """joint_probability returns correct results for no gene or trait in three-generation family"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[2], set(), set(), set())
    assert_within(p, 0.8082, 0.01, "joint probability")


@check50.check(imports)
def test_jp7():
    """joint_probability returns correct results for presence of gene and trait in three-generation family"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    p = heredity.joint_probability(FAMILIES[2], {"Rose"}, {"Ron"}, {"Ron"})
    assert_within(p, .00002406, 0.000001, "joint probability")


@check50.check(imports)
def test_update0():
    """update correctly updates for person without gene or trait"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    probs = {
        "Harry": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        "James": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        "Lily": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
    }

    heredity.update(probs, {"Lily"}, {"James"}, {"James"}, 0.02)
    assert_within(probs["Harry"]["gene"][0], 0.02, 0.0001, "value for 0 copies of gene")
    assert_within(probs["Harry"]["gene"][1], 0.00, 0.0001, "value for 1 copy of gene")
    assert_within(probs["Harry"]["gene"][2], 0.00, 0.0001, "value for 2 copies of gene")
    assert_within(probs["Harry"]["trait"][False], 0.02, 0.0001, "value for no trait")
    assert_within(probs["Harry"]["trait"][True], 0.00, 0.0001, "value for trait")


@check50.check(imports)
def test_update1():
    """update correctly updates for person with one copy of gene"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    probs = {
        "Harry": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        "James": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        "Lily": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
    }
    heredity.update(probs, {"Lily"}, {"James"}, {"James"}, 0.02)
    assert_within(probs["Lily"]["gene"][0], 0.00, 0.0001, "value for 0 copies of gene")
    assert_within(probs["Lily"]["gene"][1], 0.02, 0.0001, "value for 1 copy of gene")
    assert_within(probs["Lily"]["gene"][2], 0.00, 0.0001, "value for 2 copies of gene")
    assert_within(probs["Lily"]["trait"][False], 0.02, 0.0001, "value for no trait")
    assert_within(probs["Lily"]["trait"][True], 0.00, 0.0001, "value for trait")


@check50.check(imports)
def test_update2():
    """update correctly updates for person with two copies of gene"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    probs = {
        "Harry": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        "James": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        "Lily": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
    }
    heredity.update(probs, {"Lily"}, {"James"}, {"James"}, 0.02)
    assert_within(probs["James"]["gene"][0], 0.00, 0.0001, "value for 0 copies of gene")
    assert_within(probs["James"]["gene"][1], 0.00, 0.0001, "value for 1 copy of gene")
    assert_within(probs["James"]["gene"][2], 0.02, 0.0001, "value for 2 copies of gene")
    assert_within(probs["James"]["trait"][False], 0.00, 0.0001, "value for no trait")
    assert_within(probs["James"]["trait"][True], 0.02, 0.0001, "value for trait")


@check50.check(imports)
def test_update3():
    """update correctly updates when existing probabilities already exist"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    probs = {
        "Harry": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        "James": {"gene": {2: 0.01, 1: 0.04, 0: 0.05}, "trait": {True: 0.06, False: 0.07}},
        "Lily": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
    }
    heredity.update(probs, {"Lily"}, {"James"}, {"James"}, 0.02)
    assert_within(probs["James"]["gene"][0], 0.05, 0.0001, "value for 0 copies of gene")
    assert_within(probs["James"]["gene"][1], 0.04, 0.0001, "value for 1 copy of gene")
    assert_within(probs["James"]["gene"][2], 0.03, 0.0001, "value for 2 copies of gene")
    assert_within(probs["James"]["trait"][False], 0.07, 0.0001, "value for no trait")
    assert_within(probs["James"]["trait"][True], 0.08, 0.0001, "value for trait")


@check50.check(imports)
def test_normalize0():
    """normalize correctly normalizes probabilities"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    probs = {
        "Harry": {"gene": {2: 0.1, 1: 0.3, 0: 0.1}, "trait": {True: 0.2, False: 0.3}},
        "James": {"gene": {2: 0.01, 1: 0.01, 0: 0.02}, "trait": {True: 0.3, False: 0.3}},
        "Lily": {"gene": {2: 0, 1: 0.1, 0: 0}, "trait": {True: 0.1, False: 0}}
    }
    heredity.normalize(probs)
    assert_within(probs["Harry"]["gene"][0], 0.2, 0.0001, "value for 0 copies of gene")
    assert_within(probs["Harry"]["gene"][1], 0.6, 0.0001, "value for 1 copy of gene")
    assert_within(probs["Harry"]["gene"][2], 0.2, 0.0001, "value for 2 copies of gene")
    assert_within(probs["Harry"]["trait"][False], 0.6, 0.0001, "value for no trait")
    assert_within(probs["Harry"]["trait"][True], 0.4, 0.0001, "value for trait")


@check50.check(imports)
def test_normalize1():
    """normalize correctly normalizes probabilities when some distribution values empty"""
    sys.path = [""] + sys.path
    heredity = check50.py.import_("heredity.py")
    probs = {
        "Harry": {"gene": {2: 0.1, 1: 0.3, 0: 0.1}, "trait": {True: 0.2, False: 0.3}},
        "James": {"gene": {2: 0.01, 1: 0.01, 0: 0.02}, "trait": {True: 0.3, False: 0.3}},
        "Lily": {"gene": {2: 0, 1: 0.1, 0: 0}, "trait": {True: 0.1, False: 0}}
    }
    heredity.normalize(probs)
    assert_within(probs["Lily"]["gene"][0], 0.0, 0.0001, "value for 0 copies of gene")
    assert_within(probs["Lily"]["gene"][1], 1.0, 0.0001, "value for 1 copy of gene")
    assert_within(probs["Lily"]["gene"][2], 0.0, 0.0001, "value for 2 copies of gene")
    assert_within(probs["Lily"]["trait"][False], 0.0, 0.0001, "value for no trait")
    assert_within(probs["Lily"]["trait"][True], 1.0, 0.0001, "value for trait")
