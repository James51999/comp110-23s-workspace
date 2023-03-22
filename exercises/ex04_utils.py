"""`list` Utility Functions!"""
__author__ = "730165858"


def all(inpt: list[int], x: int) -> bool:
    """This function checks to see if all the values in a list are the same as an argument."""
    if len(inpt) == 0:
        return False
    count: int = 0
    idx: int = 0
    while idx < len(inpt):
        if x == inpt[idx]:
            count += 1
        idx += 1
    if count == len(inpt):
        return True
    else:
        return False


def max(inpt: list[int]) -> int:
    """This function checks to see what the max is from a list of numbers."""
    if len(inpt) == 0:
        raise ValueError("max() arg is an empty List")
    idx = 0
    x = inpt[0]
    
    while idx < len(inpt):
        if x < inpt[idx]:
            x = inpt[idx]
        idx += 1
    return x


def is_equal(inpt_1: list[int], inpt_2: list[int]) -> bool:
    """This funtion tests to see if two lists are equal."""
    idx = 0
    if len(inpt_1) != len(inpt_2):
        return False
    while idx < len(inpt_1):
        if inpt_1[idx] != inpt_2[idx]:
            return False
        idx += 1
    return True