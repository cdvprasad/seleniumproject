import pytest


def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"
    assert a == b, "test failed a is not equal to b"


def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"


def test_m3():
    assert True


def test_m4():
    assert False


def test_login_insta():
    assert "admin" == "admin"
