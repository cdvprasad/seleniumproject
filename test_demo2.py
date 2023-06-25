import pytest

@pytest.mark.home
def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"
    assert a == b, "test failed a is not equal to b"

@pytest.mark.home
def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.home
def test_m3():
    assert True


def test_m4():
    assert False

@pytest.mark.login
def test_login_gmail():
    assert "admin" == "admin"