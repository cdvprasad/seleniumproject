import pytest


def test_total_divisble_by_6(input_total):
    assert input_total % 6 == 0


def test_total_divisble_by_8(input_total):
    assert input_total % 8 == 0


def test_total_divisble_by_11(input_total):
    assert input_total % 11 == 0