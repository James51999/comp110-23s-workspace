"""ex05 - utils!"""
__author__ = "730165858"


def only_evens(inpt: list[int]) -> list[int]:
    """This function returns a list of the even numbers in the input list!"""
    evens: list[int] = []
    for x in inpt:
        if x % 2 == 0:
            evens.append(x)
    return evens
    

def concat(input_1: list[int], input_2: list[int]):
    """This function concatinates two input lists!"""
    new_lst = []
    for x in input_1:
        new_lst.append(x)
    for x in input_2:
        new_lst.append(x)
    return new_lst


def sub(inpt: list[int], srt_idx, end_idx):
    """This function takes a list and a start and a stop index and generates a new list with a subsed of the input between the start and stop-1!"""
    lst = []
    for x in range(srt_idx, end_idx): 
        if x < 0:
            None 
        elif x < len(inpt):
            lst.append(inpt[x])
    return lst