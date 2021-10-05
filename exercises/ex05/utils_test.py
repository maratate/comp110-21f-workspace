"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730384808"

# edge case 


def test_only_evens_empty() -> None:
    x: list[int] = []
    assert only_evens(x) == []  

# use case 


def test_only_evens_only_odds() -> None:
    x: list[int] = [3, 5, 7, 4]
    assert only_evens(x) == [4]

# use case 


def test_only_evens_find_even_intergers() -> None:
    x: list[int] = [1, 2, 4, 6]
    assert only_evens(x) == [2, 4, 6]

# edge case 


def test_sub_when_list_is_empty() -> None: 
    x: list[int] = [] 
    assert sub(x, 1, 4) == []

# use case 


def test_sub_with_indexes() -> None:
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, 0, 4) == [1, 2, 3, 4]

# use case 


def test_sub_when_start_is_less_than_1() -> None:
    x: list[int] = [10, 11, 12, 13, 14]
    assert sub(x, -1, 4) == [10, 11, 12, 13]

# edge case 


def test_concat_when_lists_are_empty() -> None:
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []

# use case 


def test_concat_2_lists() -> None:
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [5, 6, 7, 8]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8]

# use case 


def test_concat_list_with_empty_list() -> None:
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = []
    assert concat(list_1, list_2) == [1, 2, 3, 4]
