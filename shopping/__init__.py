import copy
import numpy as np
import pandas as pd
import sys

import check50
import check50.py


@check50.check()
def exists():
    """shopping.py exists"""
    check50.include("shopping.csv")
    check50.exists("shopping.py")


@check50.check(exists)
def imports():
    """shopping.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("shopping.py")


@check50.check(imports)
def load_data_lines():
    """load_data returns correct number of rows"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")
    evidence, labels = shopping.load_data("shopping.csv")
    if isinstance(evidence, pd.core.frame.DataFrame):
        evidence = evidence.values.tolist()
    expected = 12330

    if len(evidence) != expected:
        raise check50.Mismatch(f"{expected} evidence arrays",
                               f"{len(evidence)} evidence arrays")

    if len(labels) != expected:
        raise check50.Mismatch(f"{expected} labels",
                               f"{len(labels)} labels")

@check50.check(imports)
def load_data_int():
    """load_data correctly handles integer values"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")
    evidence, labels = shopping.load_data("shopping.csv")
    if isinstance(evidence, pd.core.frame.DataFrame):
        evidence = evidence.values.tolist()

    # row, col, expected
    tests = [
        (0, 0, 0),
        (2, 4, 1),
    ]
    for row, col, expected in tests:
        if evidence[row][col] != expected:
            raise check50.Mismatch(str(expected), str(evidence[row][col]))


@check50.check(imports)
def load_data_float():
    """load_data correctly handles floating-point values"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")
    evidence, labels = shopping.load_data("shopping.csv")
    if isinstance(evidence, pd.core.frame.DataFrame):
        evidence = evidence.values.tolist()

    # row, col, expected
    tests = [
        (0, 6, 0.2),
        (3, 7, 0.14),
    ]
    for row, col, expected in tests:
        if evidence[row][col] != expected:
            raise check50.Mismatch(str(expected), str(evidence[row][col]))


@check50.check(imports)
def load_data_month():
    """load_data correctly handles month transformations"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")
    evidence, labels = shopping.load_data("shopping.csv")
    if isinstance(evidence, pd.core.frame.DataFrame):
        evidence = evidence.values.tolist()

    # row, col, expected
    tests = [
        (0, 10, 1),
        (256, 10, 2),
    ]
    for row, col, expected in tests:
        if evidence[row][col] != expected:
            raise check50.Mismatch(str(expected), str(evidence[row][col]))


@check50.check(imports)
def load_data_visitor():
    """load_data correctly handles boolean values"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")
    evidence, labels = shopping.load_data("shopping.csv")
    if isinstance(evidence, pd.core.frame.DataFrame):
        evidence = evidence.values.tolist()

    # row, col, expected
    tests = [
        (0, 15, 1),
        (93, 15, 0),
    ]
    for row, col, expected in tests:
        if evidence[row][col] != expected:
            raise check50.Mismatch(str(expected), str(evidence[row][col]))

@check50.check(imports)
def train_model():
    """train_model returns a k-nearest-neighbor classifier"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")
    evidence = [
        [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0.0, 0, 0.0, 2, 64.0, 0.0, 0.1, 0.0, 0.0, 1, 2, 2, 1, 2, 1, 0],
        [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 4, 1, 9, 3, 1, 0],
        [0, 0.0, 0, 0.0, 2, 2.666666667, 0.05, 0.14, 0.0, 0.0, 1, 3, 2, 2, 4, 1, 0],
        [0, 0.0, 0, 0.0, 10, 627.5, 0.02, 0.05, 0.0, 0.0, 1, 3, 3, 1, 4, 1, 1],
        [0, 0.0, 0, 0.0, 19, 154.2166667, 0.015789474, 0.024561404, 0.0, 0.0, 1, 2, 2, 1, 3, 1, 0],
        [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.4, 1, 2, 4, 3, 3, 1, 0],
        [1, 0.0, 0, 0.0, 0, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 2, 1, 5, 1, 1],
        [0, 0.0, 0, 0.0, 2, 37.0, 0.0, 0.1, 0.0, 0.8, 1, 2, 2, 2, 3, 1, 0],
        [0, 0.0, 0, 0.0, 3, 738.0, 0.0, 0.022222222, 0.0, 0.4, 1, 2, 4, 1, 2, 1, 0]
    ]
    labels = [0, 0, 0, 1, 0, 1, 0, 1, 0, 1]

    # Model
    model = shopping.train_model(evidence, labels)

    if "KNeighborsClassifier" not in str(type(model)):
        raise check50.Mismatch("KNeighborsClassifier", str(type(model)))


@check50.check(imports)
def train_model_n():
    """train_model returns a k-nearest-neighbor classifier with n = 1"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")
    evidence = [
        [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0.0, 0, 0.0, 2, 64.0, 0.0, 0.1, 0.0, 0.0, 1, 2, 2, 1, 2, 1, 0],
        [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 4, 1, 9, 3, 1, 0],
        [0, 0.0, 0, 0.0, 2, 2.666666667, 0.05, 0.14, 0.0, 0.0, 1, 3, 2, 2, 4, 1, 0],
        [0, 0.0, 0, 0.0, 10, 627.5, 0.02, 0.05, 0.0, 0.0, 1, 3, 3, 1, 4, 1, 1],
        [0, 0.0, 0, 0.0, 19, 154.2166667, 0.015789474, 0.024561404, 0.0, 0.0, 1, 2, 2, 1, 3, 1, 0],
        [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.4, 1, 2, 4, 3, 3, 1, 0],
        [1, 0.0, 0, 0.0, 0, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 2, 1, 5, 1, 1],
        [0, 0.0, 0, 0.0, 2, 37.0, 0.0, 0.1, 0.0, 0.8, 1, 2, 2, 2, 3, 1, 0],
        [0, 0.0, 0, 0.0, 3, 738.0, 0.0, 0.022222222, 0.0, 0.4, 1, 2, 4, 1, 2, 1, 0]
    ]
    labels = [0, 0, 0, 1, 0, 1, 0, 1, 0, 1]

    # Model
    model = shopping.train_model(evidence, labels)

    if model.n_neighbors != 1:
        raise check50.Mismatch("1", str(model.n_neighbors))


@check50.check(imports)
def evaluate0():
    """evaluate provides correct values for sensitivity"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")

    data = [1, 1, 1, 1, 0, 0, 0, 0]
    predictions = np.array([1, 1, 1, 0, 0, 0, 1, 1])
    sensitivity, specificity = shopping.evaluate(data, predictions)

    expected = 0.75
    if sensitivity != expected:
        raise check50.Mismatch(str(expected), str(sensitivity))


@check50.check(imports)
def evaluate1():
    """evaluate provides correct values for specificity"""

    # Setup
    sys.path = [""] + sys.path
    shopping = check50.py.import_("shopping.py")

    data = [1, 1, 1, 1, 0, 0, 0, 0]
    predictions = np.array([1, 1, 1, 0, 0, 0, 1, 1])
    sensitivity, specificity = shopping.evaluate(data, predictions)

    expected = 0.5
    if specificity != expected:
        raise check50.Mismatch(str(expected), str(specificity))

