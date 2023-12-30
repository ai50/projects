import os
import sys

import check50
import check50.py

def assert_within(actual, expected, tolerance, name="value"):
    lower = expected - tolerance
    upper = expected + tolerance
    if not lower <= actual <= upper:
        raise check50.Failure(f"expected {name} to be in range [{lower}, {upper}], got {actual} instead")


def assert_idf_within(actual, expected, tolerance=0.01):
    for word in expected:
        assert_within(actual[word], expected[word], tolerance, name=f"IDF value for '{word}'")


@check50.check()
def exists():
    """questions.py exists"""
    os.system("python3 -m nltk.downloader stopwords")
    check50.exists("questions.py")
    check50.include("files")


@check50.check(exists)
def imports():
    """questions.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("questions.py")


@check50.check(imports)
def load_files():
    """load_files loads text files into memory"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    expected = {"a.txt": "this is file a", "b.txt": "this is file b"}
    actual = questions.load_files("files")
    actual = {filename: actual[filename].strip() for filename in actual}

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def tokenize0():
    """tokenize splits document into words"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    expected = ["one", "two", "three", "four"]
    actual = questions.tokenize("one two three four")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def tokenize1():
    """tokenize converts words to lowercase"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    expected = ["one", "two", "three", "four"]
    actual = questions.tokenize("ONE Two thREE FOUr")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def tokenize2():
    """tokenize filters out punctuation"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    expected = ["one", "two", "three", "four", "five"]
    actual = questions.tokenize("one two. three four. five.")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def tokenize3():
    """tokenize filters out stopwords"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    expected = ["one", "two", "three", "four", "five", "six"]
    actual = questions.tokenize("me one myself two before three more four should five what six")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def tokenize4():
    """tokenize handles stopwords, punctuation, and capitalization together"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    expected = ["one", "two", "three", "four", "five", "six"]
    actual = questions.tokenize("me OnE myself two Before three. more four should five what six.")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def compute_idfs0():
    """compute_idfs calculates IDFs for simple set of documents"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"]
    }
    expected = {
        "one": 0.0,
        "two": 0.405,
        "three": 0.405,
        "four": 1.099
    }
    actual = questions.compute_idfs(documents)
    assert_idf_within(actual, expected)


@check50.check(imports)
def compute_idfs1():
    """compute_idfs calculates IDFs for more complex set of documents"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two"],
        "e": ["five"]
    }
    expected = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    actual = questions.compute_idfs(documents)
    assert_idf_within(actual, expected)


@check50.check(imports)
def compute_idfs2():
    """compute_idfs handles documents that contain repeated words"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two", "one", "one"],
        "c": ["one", "three", "four", "three", "three"],
        "d": ["one", "two", "two", "two"],
        "e": ["five", "five", "five", "five", "five"]
    }
    expected = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    actual = questions.compute_idfs(documents)
    assert_idf_within(actual, expected)


@check50.check(imports)
def top_files0():
    """top_files finds file that matches query"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"five"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 1

    expected = ["e"]
    actual = questions.top_files(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def top_files1():
    """top_files correctly accounts for IDF"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"one", "two", "three", "five"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 1

    expected = ["a"]
    actual = questions.top_files(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def top_files2():
    """top_files correctly accounts for term frequency"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"one", "two", "three", "five"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two", "one", "two", "one", "two"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 1

    expected = ["d"]
    actual = questions.top_files(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def top_files3():
    """top_files handles returning multiple files"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"one", "two", "three", "five"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 2

    expected = ["a", "e"]
    actual = questions.top_files(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def top_sentences0():
    """top_sentences correctly accounts for matching word measure"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"one", "two", "three", "five"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 1

    expected = ["a"]
    actual = questions.top_sentences(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def top_sentences1():
    """top_sentences correctly weights words by IDF"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"one", "two", "five"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 1

    expected = ["e"]
    actual = questions.top_sentences(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def top_sentences2():
    """top_sentences correctly considers query term density"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"one"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four"],
        "d": ["one", "two", "one"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 1

    expected = ["d"]
    actual = questions.top_sentences(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def top_sentences3():
    """top_sentences handles returning multiple sentences"""

    # Setup
    sys.path = [""] + sys.path
    questions = check50.py.import_("questions.py")

    query = {"one"}
    documents = {
        "a": ["one", "two", "three"],
        "b": ["one", "two"],
        "c": ["one", "three", "four", "one", "one"],
        "d": ["one", "two", "one"],
        "e": ["five"]
    }
    idfs = {
        "one": 0.223,
        "two": 0.511,
        "three": 0.916,
        "four": 1.609,
        "five": 1.609
    }
    n = 2

    expected = ["d", "c"]
    actual = questions.top_sentences(query, documents, idfs, n)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))
