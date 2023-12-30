import copy
import sys

import check50
import check50.py


def assert_within(actual, expected, tolerance, name="value"):
    lower = expected - tolerance
    upper = expected + tolerance
    if not lower <= actual <= upper:
        raise check50.Failure(f"expected {name} to be in range [{lower}, {upper}], got {actual} instead")


@check50.check()
def exists():
    """nim.py exists"""
    check50.exists("nim.py")


@check50.check(exists)
def imports():
    """nim.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("nim.py")


@check50.check(imports)
def get_q_value0():
    """get_q_value returns correct value when Q-value exists"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI()
    ai.q = {
        ((1, 2, 3, 4), (0, 1)): 0.6,
        ((1, 2, 2, 4), (0, 1)): 0.5
    }

    expected = 0.6
    actual = ai.get_q_value([1, 2, 3, 4], (0, 1))
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def get_q_value1():
    """get_q_value returns correct value when Q-value does not exist"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI()
    ai.q = {
        ((1, 2, 3, 4), (0, 1)): 0.6,
        ((1, 2, 2, 4), (0, 1)): 0.5
    }

    expected = 0
    actual = ai.get_q_value([1, 2, 3, 4], (1, 1))
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def update_q_value0():
    """update_q_value increases Q-value when new estimated value is higher"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI()
    ai.q = {
        ((1, 2, 3, 4), (0, 1)): 0.6,
        ((1, 2, 2, 4), (0, 1)): 0.5
    }

    expected = 0.7
    ai.update_q_value([1, 2, 3, 4], (0, 1), 0.6, 0, 0.8)
    actual = ai.q[((1, 2, 3, 4), (0, 1))]
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def update_q_value1():
    """update_q_value decreases Q-value when new estimated value is lower"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI()
    ai.q = {
        ((1, 2, 3, 4), (0, 1)): 0.6,
        ((1, 2, 2, 4), (0, 1)): 0.5
    }

    expected = 0.4
    ai.update_q_value([1, 2, 3, 4], (0, 1), 0.6, 0.2, 0)
    actual = ai.q[((1, 2, 3, 4), (0, 1))]
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def update_q_value2():
    """update_q_value adds Q-value when it didn't exist before"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI()
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): 0.5
    }

    expected = 0.2
    ai.update_q_value([1, 2, 3, 4], (0, 1), 0, 0.4, 0)
    actual = ai.q[((1, 2, 3, 4), (0, 1))]
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def update_q_value3():
    """update_q_value handles different values for alpha"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI(alpha=0.75)
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): 0.5
    }

    expected = 0.3
    ai.update_q_value([1, 2, 3, 4], (0, 1), 0, 0.4, 0)
    actual = ai.q[((1, 2, 3, 4), (0, 1))]
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def best_future_reward0():
    """best_future_reward finds best action with limited Q data"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI(alpha=0.75)
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): 0.3,
        ((1, 2, 2, 4), (1, 1)): 0.2,
        ((1, 2, 2, 4), (1, 2)): 0.4,
        ((1, 2, 2, 4), (2, 1)): 0.25,
    }

    expected = 0.4
    actual = ai.best_future_reward([1, 2, 2, 4])
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def best_future_reward1():
    """best_future_reward finds best action with more Q data"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI(alpha=0.75)
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): 0.3,
        ((1, 2, 2, 4), (1, 1)): 0.2,
        ((1, 2, 2, 4), (1, 2)): 0.4,
        ((1, 2, 2, 4), (2, 1)): 0.25,
        ((1, 2, 2, 5), (2, 1)): 0.5,
    }

    expected = 0.4
    actual = ai.best_future_reward([1, 2, 2, 4])
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def best_future_reward2():
    """best_future_reward finds best action when only aware of bad actions"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI(alpha=0.75)
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): -0.3,
        ((1, 2, 2, 4), (1, 1)): -0.2,
        ((1, 2, 2, 4), (1, 2)): -0.4,
        ((1, 2, 2, 4), (2, 1)): -0.25,
        ((1, 2, 2, 5), (2, 1)): -0.5,
    }

    expected = 0
    actual = ai.best_future_reward([1, 2, 2, 4])
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def best_future_reward3():
    """best_future_reward handles case where game is over"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI(alpha=0.75)
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): -0.3,
        ((1, 2, 2, 4), (1, 1)): -0.2,
        ((1, 2, 2, 4), (1, 2)): -0.4,
        ((1, 2, 2, 4), (2, 1)): -0.25,
        ((1, 2, 2, 5), (2, 1)): -0.5,
    }

    expected = 0
    actual = ai.best_future_reward([0, 0, 0, 0])
    assert_within(actual, expected, 0.001, "q-value")


@check50.check(imports)
def choose_action0():
    """choose_action is able to greedily choose action"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI(alpha=0.75)
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): 0.3,
        ((1, 2, 2, 4), (1, 1)): 0.2,
        ((1, 2, 2, 4), (1, 2)): 0.4,
        ((1, 2, 2, 4), (2, 1)): 0.25,
        ((1, 2, 2, 5), (2, 1)): 0.5,
    }

    expected = (1, 2)
    actual = ai.choose_action([1, 2, 2, 4], epsilon=False)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def choose_action1():
    """choose_action is able to choose actions with epsilon-greedy"""

    # Setup
    sys.path = [""] + sys.path
    nim = check50.py.import_("nim.py")
    ai = nim.NimAI(epsilon=0.5)
    ai.q = {
        ((1, 2, 2, 4), (0, 1)): 0.3,
        ((1, 2, 2, 4), (1, 1)): 0.2,
        ((1, 2, 2, 4), (1, 2)): 0.4,
        ((1, 2, 2, 4), (2, 1)): 0.25,
        ((1, 2, 2, 5), (2, 1)): 0.5,
    }

    expected = (1, 2)
    total = 1000
    count = 0
    for i in range(total):
        action = ai.choose_action([1, 2, 2, 4], epsilon=True)
        if action == expected:
            count += 1

    assert_within(count / total, 0.5, 0.3, "proportion of greedy moves")
