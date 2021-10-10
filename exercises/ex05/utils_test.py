"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730384808"

# edge case 


def test_only_evens_empty() -> None:
    """Returns empty list with no even integers."""
    x: list[int] = []
    assert only_evens(x) == []  

# use case 


def test_only_evens_only_odds() -> None:
    """Returns even empty list because there are no even integers."""
    x: list[int] = [3, 5, 7]
    assert only_evens(x) == []

# use case 


def test_only_evens_find_even_intergers() -> None:
    """Returns evens from list."""
    x: list[int] = [1, 2, 4, 6]
    assert only_evens(x) == [2, 4, 6]

# edge case 


def test_sub_when_list_is_empty() -> None: 
    """Returns empty list."""
    x: list[int] = [] 
    assert sub(x, 1, 4) == []

# use case 


def test_sub_with_indexes() -> None:
    """Returns intergers between indexes."""
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, 0, 4) == [1, 2, 3, 4]

# use case 


def test_sub_when_start_is_less_than_1() -> None:
    """Returns integers between indexes when start index is less than 1."""
    x: list[int] = [10, 11, 12, 13, 14]
    assert sub(x, -1, 4) == [10, 11, 12, 13]

# edge case 


def test_concat_when_lists_are_empty() -> None:
    """Adds two empty lists."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []

# use case 


def test_concat_2_lists() -> None:
    """Adds the integers from two lists."""
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [5, 6, 7, 8]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8]

# use case 


def test_concat_list_with_empty_list() -> None:
    """Adds the intergers from a list and an empty list."""
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = []
    assert concat(list_1, list_2) == [1, 2, 3, 4]
