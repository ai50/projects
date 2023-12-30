import sys

import check50
import check50.py

from nltk import Tree


@check50.check()
def exists():
    """parser.py exists"""
    check50.exists("parser.py")


@check50.check(exists)
def imports():
    """parser.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("parser.py")


@check50.check(imports)
def preprocess0():
    """preprocess tokenizes words"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    actual = parser.preprocess("one two three four")
    expected = ["one", "two", "three", "four"]

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def preprocess1():
    """preprocess converts words to lowercase"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    actual = parser.preprocess("ONE TwO tHREE Four five")
    expected = ["one", "two", "three", "four", "five"]

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def preprocess2():
    """preprocess removes tokens without alphabetic characters"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    actual = parser.preprocess("one two. three four five. six seven.")
    expected = ["one", "two", "three", "four", "five", "six", "seven"]

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def parse0():
    """parser can parse simple sentence"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    sentence = ["holmes", "sat"]
    success = False
    try:
        trees = list(parser.parser.parse(sentence))
        if trees:
            success = True
    except ValueError:
        pass

    if not success:
        raise check50.Failure(f"Could not parse sentence: \"{' '.join(sentence)}\".")


@check50.check(imports)
def parse1():
    """parser can parse more complex sentences"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    sentence = ["i", "had", "a", "country", "walk", "on", "thursday", "and",
                "came", "home", "in", "a", "dreadful", "mess"]
    success = False
    try:
        trees = list(parser.parser.parse(sentence))
        if trees:
            success = True
    except ValueError:
        pass

    if not success:
        raise check50.Failure(f"Could not parse sentence: \"{' '.join(sentence)}\".")


@check50.check(imports)
def parse2():
    """parser can generalize to other similar sentences"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    sentence = ["holmes", "smiled", "to", "himself", "and", "he", "lit", "the", "pipe"]
    success = False
    try:
        trees = list(parser.parser.parse(sentence))
        if trees:
            success = True
    except ValueError:
        pass

    if not success:
        raise check50.Failure(f"Could not parse sentence: \"{' '.join(sentence)}\".")


@check50.check(imports)
def parse2():
    """parser avoids over-generalizing to syntactically incorrect sentences"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    sentence = ["the", "smiled", "and", "he", "arrived", "thursday"]
    success = False
    try:
        trees = list(parser.parser.parse(sentence))
        if trees:
            success = True
    except ValueError:
        pass

    if success:
        raise check50.Failure(f"Parsed invalid sentence: \"{' '.join(sentence)}\".")


@check50.check(imports)
def np_chunk0():
    """np_chunk identifies noun phrase"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    tree = Tree('S',
            [Tree('NP',
                [Tree('Nb',
                    [Tree('N', ['he'])]
                 )]
             ),
             Tree('VP',
                [Tree('V', ['smiled'])]
             )]
            )
    nps = set(" ".join(t.flatten()) for t in parser.np_chunk(tree))
    expected = set(["he"])
    if expected != nps:
        raise check50.Mismatch(str(expected), str(nps))


@check50.check(imports)
def np_chunk1():
    """np_chunk finds noun phrases that don't contain other noun phrases"""

    # Setup
    sys.path = [""] + sys.path
    parser = check50.py.import_("parser.py")

    tree = Tree('S', [Tree('NP', [Tree('Nb', [Tree('N', ['holmes'])])]), Tree('VP', [Tree('VP', [Tree('V', ['sat'])]), Tree('PP', [Tree('P', ['in']), Tree('NP', [Tree('Det', ['the']), Tree('Nb', [Tree('Nb', [Tree('N', ['armchair'])]), Tree('PP', [Tree('P', ['in']), Tree('NP', [Tree('Det', ['the']), Tree('Nb', [Tree('N', ['home'])])])])])])])])])
    nps = set(" ".join(t.flatten()) for t in parser.np_chunk(tree))
    expected = set(["holmes", "the home"])
    if expected != nps:
        raise check50.Mismatch(str(expected), str(nps))
