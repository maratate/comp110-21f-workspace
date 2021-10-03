"""List utility functions."""

__author__ = "730384808"

# TODO: Implement your functions here.
  

def all(x: list[int], y: int) -> bool:
    """All function: Return True if integer equals all the items in list."""
    i: int = 0
    while (len(x) - 1) >= i: 
        if i == len(x) - 1:
            if x[i] == y:
                return True    
        if x[i] == y:
            i += 1
        else:
            return False
    return False 
            

def is_equal(x: list[int], y: list[int]) -> bool: 
    """is_equal function: Return True is all the items in the list are the same."""
    i: int = 0
    if len(x) == len(y):
        if 0 == len(x) and 0 == len(y):
            return True 
        while i <= ((len(x) - 1)) or (len(y) - 1):
            if i == (len(x) - 1) or (len(y) - 1):
                if x[i] == y[i]:
                    return True
            if x[i] == y[i]:
                i += 1 
            else:
                return False 
            if len(x) != len(y):
                return False 
    return False 


def max(input: list[int]) -> int:
    """Max function: returns integer with the largest value."""
    maximum = input[0] 
    if len(input) == 0: 
        raise ValueError("max() arg is empty List")
    for x in input: 
        if x > maximum:
            maximum = x 
    return maximum 