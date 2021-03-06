import repeat
import pytest


def test_only_one_repeats():
    a = [1, 2, 3, 4]
    assert repeat.largest_repeat(a) == 1


def test_two_and_one_repeats():
    a = [1, 2, 2, 3, 3]
    assert repeat.largest_repeat(a) == 2


def test_three_and_four_repeats():
    a = [1, 2, 3, 3, 3, 4, 4, 4, 4]
    assert repeat.largest_repeat(a) == 4
