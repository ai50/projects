import os
import sys

import check50
import check50.py

@check50.check()
def exists():
    """degrees.py exists"""
    check50.exists("degrees.py")
    check50.include("small")
    if not os.path.exists("util.py"):
        check50.include("util.py")


@check50.check(exists)
def imports():
    """degrees.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("degrees.py")


@check50.check(imports)
def path1():
    """degrees.py finds a path of length 1"""
    sys.path = [""] + sys.path
    degrees = check50.py.import_("degrees.py")
    degrees.load_data("small")
    bacon = degrees.person_id_for_name("Kevin Bacon")
    cruise = degrees.person_id_for_name("Tom Cruise")
    path = degrees.shortest_path(bacon, cruise)
    if len(path) != 1:
        raise check50.Mismatch("1", str(len(path)))

@check50.check(imports)
def path_none():
    """degrees.py identifies when path does not exist"""
    sys.path = [""] + sys.path
    degrees = check50.py.import_("degrees.py")
    degrees.load_data("small")
    hoffman = degrees.person_id_for_name("Dustin Hoffman")
    watson = degrees.person_id_for_name("Emma Watson")
    path = degrees.shortest_path(hoffman, watson)
    if path is not None:
        raise check50.Mismatch("no path", str(path))

@check50.check(imports)
def path2():
    """degrees.py finds a path of length 2"""
    sys.path = [""] + sys.path
    degrees = check50.py.import_("degrees.py")
    degrees.load_data("small")
    hanks = degrees.person_id_for_name("Tom Hanks")
    patinkin = degrees.person_id_for_name("Mandy Patinkin")
    path = degrees.shortest_path(hanks, patinkin)
    if len(path) != 2:
        raise check50.Mismatch("2", str(len(path)))
    expected = [('109830', '705'), ('93779', '1597')]
    if path != expected:
        raise check50.Mismatch(str(expected), str(path))

@check50.check(imports)
def path4():
    """degrees.py finds a path of length 4"""
    sys.path = [""] + sys.path
    degrees = check50.py.import_("degrees.py")
    degrees.load_data("small")
    wright = degrees.person_id_for_name("Robin Wright")
    hoffman = degrees.person_id_for_name("Dustin Hoffman")
    path = degrees.shortest_path(wright, hoffman)
    if len(path) != 4:
        raise check50.Mismatch("4", str(len(path)))

@check50.check(imports)
def path0():
    """degrees.py finds a path of length 0"""
    sys.path = [""] + sys.path
    degrees = check50.py.import_("degrees.py")
    degrees.load_data("small")
    wright = degrees.person_id_for_name("Robin Wright")
    path = degrees.shortest_path(wright, wright)
    if len(path) != 0:
        raise check50.Mismatch("0", str(len(path)))
