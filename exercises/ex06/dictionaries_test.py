"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest
__author__ = "123456789"


def test_invert_empty() -> None:
    """Returns an empty dictionary."""
    empty_dictionary: dict[str, str] = {}
    assert invert(empty_dictionary) == {}


def test_key_error_invert() -> None:
    """Raises a key error when keys are duplicated."""
    with pytest.raises(KeyError):
        dictionary: dict[str, str] = {"a": "x", "b": "x", "c": "z"}
        invert(dictionary)


def test_normal_dictionary() -> None:
    """Inverts key and value in a dictionary."""
    dictionary: dict[str, str] = {"a": "x", "b": "y", "c": "z"}
    assert invert(dictionary) == {"x": "a", "y": "b", "z": "c"}


def test_favorite_color_empty() -> None:
    """Returns an empty string."""
    empty_dictionary: dict[str, str] = {}
    assert favorite_color(empty_dictionary) == ""


def test_favorite_color_normal_dictionary() -> None:
    """Returns the color that appears most frequently in dictionary."""
    dictionary: dict[str, str] = {"mara": "red", "anna": "purple", "austin": "purple", "abby": "green"}
    assert favorite_color(dictionary) == "purple"


def test_favorite_color_tie() -> None:
    """Returns the color that appears first in the dictionary because there is a tie."""
    dictionary: dict[str, str] = {"mara": "red", "anna": "purple", "austin": "purple", "abby": "red"}
    assert favorite_color(dictionary) == "red"


def test_count_empty() -> None:
    """Returns an empty dictionary."""
    intial_list: list[str] = []
    assert count(intial_list) == {}


def test_count_no_repeats() -> None:
    """Returns a dictionary with values from intial list."""
    intial_list: list[str] = ["mara", "elizabeth", "daly"]
    assert count(intial_list) == {"mara": 1, "elizabeth": 1, "daly": 1}


def test_count_with_repeats() -> None:
    """Returns a dictionary with values from intial list with increased values for repeats."""
    intial_list: list[str] = ["mara", "elizabeth", "daly", "mara", "daly"]
    assert count(intial_list) == {"mara": 2, "elizabeth": 1, "daly": 2}
