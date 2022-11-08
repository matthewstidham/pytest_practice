#! /usr/bin/env python3

def f():
    return 3


def test_function():
    assert f() == 4


def test_2():
    assert f() % 2 == 0
