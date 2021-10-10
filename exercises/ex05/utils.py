"""List utility functions part 2."""

__author__ = "730384808"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]: 
    """Return even integers from the list."""
    i: int = 0 
    list_evens: list[int] = []
    for x in xs: 
        if x % 2 == 0:
            list_evens.append(x)
        i += 1
    return (list_evens)


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Return integers bewteen 2 indexes."""
    list_2: list[int] = []
    if x == []:
        return list_2 
    if start == len(x):
        return list_2
    if start < 0:
        start = 0 
    if end > (len(x)):
        end = (len(x))
    while start <= (end - 1):
        list_2.append(x[start])
        start += 1 
    return list_2 
    

def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Concat the integers of two lists."""
    list_3: list[int] = []
    for x in list_1:
        list_3.append(x)
    for x in list_2:
        list_3.append(x)
    return list_3
