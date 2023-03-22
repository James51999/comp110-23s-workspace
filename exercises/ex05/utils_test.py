"""Test funtions from utils!"""
__author__ = "730165858"
from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_use_1() -> None:
    """Function to test only_evens usage case!"""
    test_lst: list[int] = [1, 2, 3]
    assert only_evens(test_lst) == [2]


def test_only_evens_use_2() -> None:
    """Function to test only_evens usage case!"""
    test_lst: list[int] = [1, 5, 3]
    assert only_evens(test_lst) == []


def test_only_evens_edge() -> None:
    """Function to test only_evens edge case!"""
    test_lst: list[int] = []
    assert only_evens(test_lst) == []


def test_concat_use_1() -> None:
    """Function to test concat usage case!"""
    test_lst_1: list[int] = [1, 2, 3]
    test_lst_2: list[int] = [4, 5, 6]
    assert concat(test_lst_1, test_lst_2) == [1, 2, 3, 4, 5, 6]


def test_concat_use_2() -> None:
    """Function to test concat usage case!"""
    test_lst_1: list[int] = [5, 4, 3]
    test_lst_2: list[int] = [2, 1]
    assert concat(test_lst_1, test_lst_2) == [5, 4, 3, 2, 1]


def test_concat_edge() -> None:
    """Function to test only_evens edge case!"""
    test_lst_1: list[int] = [5, 4, 3]
    test_lst_2: list[int] = []
    assert concat(test_lst_1, test_lst_2) == [5, 4, 3]


def test_sub_use_1() -> None:
    """Function to test sub usage case!"""
    test_list: list[int] = [10, 20, 30, 40]
    test_srt: int = 1
    test_end: int = 3
    assert sub(test_list, test_srt, test_end) == [20, 30]
   

def test_sub_use_2() -> None:
    """Function to test sub usage case!"""
    test_list: list[int] = [10, 20, 30, 40, 100, 400, 2, 6]
    test_srt: int = 2
    test_end: int = 6
    assert sub(test_list, test_srt, test_end) == [30, 40, 100, 400]


def test_sub_edge() -> None:
    """Function to test only_evens edge case!"""
    test_list: list[int] = [4, 12, 8]
    test_srt: int = 2
    test_end: int = 6
    assert sub(test_list, test_srt, test_end) == [8]