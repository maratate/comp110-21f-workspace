"""Utility functions."""

__author__ = "123456789"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # open a handle to data file 
    file_handle = open(filename, "r", encoding="utf8")
    # prepare to read the data file as a CSV rather than just strings 
    csv_reader = DictReader(file_handle)
    # read each row of the CSV line by line 
    for row in csv_reader:
        result.append(row)
    # close the file when were done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result 


def head(x: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """Return a dict with the first N rows."""
    result: dict[str, list[str]] = {}
    if number_rows >= len(x):
        return x 
    else:
        for column in x:
            i: int = 0 
            new_list: list[str] = []
            while i < number_rows:
                new_list.append(x[column][i])
                i += 1 
            result[column] = new_list
    return result 


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Return a dict with subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in y:
        i: int = 0
        while i < len(y):
            result[column] = x[column]
            i += 1 
    return result 


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return a dict with two column based tables combined."""
    result: dict[str, list[str]] = {}
    for column in x:
        result[column] = x[column]
    for column in y:
        if column in result:
            result[column] = x[column] + y[column]
        else:
            result[column] = y[column]
    return result


def count(x: list[str]) -> dict[str, int]:
    """Return a dict that counts the number of times the value was in the input lists."""
    result: dict[str, int] = {}
    for key in x:
        if key in result:
            result[key] += 1 
        else:
            result[key] = 1 
    return result 
