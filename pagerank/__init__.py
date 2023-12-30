import sys

import check50
import check50.py

CORPORA = [
    # 0: simple
    {
        "1": {"2"},
        "2": {"1", "3"},
        "3": {"2", "4"},
        "4": {"2"}
    },

    # 1: slightly more involved
    {
        "1": {"2", "3"},
        "2": {"1", "3", "4"},
        "3": {"4", "5"},
        "4": {"1", "2", "3", "6"},
        "5": {"3"},
        "6": {"1", "2", "3"}
    },

    # 2: disjoint
    {
        "1": {"2"},
        "2": {"1", "3"},
        "3": {"2", "4"},
        "4": {"2"},
        "5": {"6"},
        "6": {"5", "7"},
        "7": {"6", "8"},
        "8": {"6"}
    },

    # 3: no links
    {
        "1": {"2"},
        "2": {"1", "3"},
        "3": {"2", "4", "5"},
        "4": {"1", "2"},
        "5": set()
    }
]

RANKS = [
    # 0: simple
    {
        "1": 0.21991,
        "2": 0.42921,
        "3": 0.21991,
        "4": 0.13096
    },

    # 1: slightly more involved
    {
        "1": 0.12538,
        "2": 0.13922,
        "3": 0.31297,
        "4": 0.19746,
        "5": 0.15801,
        "6": 0.06696
    },

    # 2: disjoint
    {
        "1": 0.10996,
        "2": 0.21461,
        "3": 0.10996,
        "4": 0.06548,
        "5": 0.10996,
        "6": 0.21461,
        "7": 0.10996,
        "8": 0.06548
    },

    # 3: no links
    {
        "1": 0.24178,
        "2": 0.35320,
        "3": 0.19773,
        "4": 0.10364,
        "5": 0.10364
    }
]

# ranks for just corpus 0 with damping factor 0.60
RANK_0_60 = {
    "1": 0.21893,
    "2": 0.39645,
    "3": 0.21893,
    "4": 0.16568
}


def assert_within(actual, expected, tolerance, name="value"):
    lower = expected - tolerance
    upper = expected + tolerance
    if not lower <= actual <= upper:
        raise check50.Failure(f"expected {name} to be in range [{lower}, {upper}], got {actual} instead")


def assert_distribution_within(actual, expected, tolerance):
    for value in expected:
        if value in actual:
            assert_within(actual[value], expected[value], tolerance, name=f"pagerank {value}")
        else:
            raise check50.Failure(f"no pagerank found for page {value}")


def log_corpus(corpus, damping):
    check50.log(f"testing on corpus {corpus} with damping factor {damping}...")


@check50.check()
def exists():
    """pagerank.py exists"""
    check50.exists("pagerank.py")


@check50.check(exists)
def imports():
    """pagerank.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("pagerank.py")


@check50.check(imports)
def test_sample0():
    """sample_pagerank returns correct results for simple corpus"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[0].copy()
    expected = RANKS[0]
    tolerance = 0.05
    log_corpus(corpus, damping)
    actual = pr.sample_pagerank(corpus, damping, 10000)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_sample1():
    """sample_pagerank returns correct results for complex corpus"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[1].copy()
    expected = RANKS[1]
    tolerance = 0.05
    log_corpus(corpus, damping)
    actual = pr.sample_pagerank(corpus, damping, 10000)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_sample2():
    """sample_pagerank returns correct results for corpus with disjoint sets of pages"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[2].copy()
    expected = RANKS[2]
    tolerance = 0.05
    log_corpus(corpus, damping)
    actual = pr.sample_pagerank(corpus, damping, 10000)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_sample3():
    """sample_pagerank returns correct results for corpus with pages without links"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[3].copy()
    expected = RANKS[3]
    tolerance = 0.05
    log_corpus(corpus, damping)
    actual = pr.sample_pagerank(corpus, damping, 10000)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_iterate0():
    """iterate_pagerank returns correct results for simple corpus"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[0].copy()
    expected = RANKS[0]
    tolerance = 0.002
    log_corpus(corpus, damping)
    actual = pr.iterate_pagerank(corpus, damping)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_iterate1():
    """iterate_pagerank returns correct results for complex corpus"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[1].copy()
    expected = RANKS[1]
    tolerance = 0.002
    log_corpus(corpus, damping)
    actual = pr.iterate_pagerank(corpus, damping)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_iterate2():
    """iterate_pagerank returns correct results for corpus with disjoint sets of pages"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[2].copy()
    expected = RANKS[2]
    tolerance = 0.002
    log_corpus(corpus, damping)
    actual = pr.iterate_pagerank(corpus, damping)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_iterate3():
    """iterate_pagerank returns correct results for corpus with pages without links"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.85
    corpus = CORPORA[3].copy()
    expected = RANKS[3]
    tolerance = 0.002
    log_corpus(corpus, damping)
    actual = pr.iterate_pagerank(corpus, damping)
    assert_distribution_within(actual, expected, tolerance)


@check50.check(imports)
def test_iterate4():
    """iterate_pagerank returns correct results for different values for damping factor"""
    sys.path = [""] + sys.path
    pr = check50.py.import_("pagerank.py")
    damping = 0.60
    corpus = CORPORA[0].copy()
    expected = RANK_0_60
    tolerance = 0.002
    log_corpus(corpus, damping)
    actual = pr.iterate_pagerank(corpus, damping)
    assert_distribution_within(actual, expected, tolerance)
