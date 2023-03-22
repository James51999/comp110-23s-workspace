def zip(strings: list[str], integers: list[int]) -> dict[str,int]:
    """Takes a list of ints and a list strings and combines them to make a dictionary. the strings are the keys and ints are the values!"""
    dictionary = {}
    #check that the lists are the same lengths and not zero
    if (len(strings) != len(integers)) or (len(strings) == 0):
        return dictionary
    else:
        #creat a dictionary probably using two for loops
        idx = 0
        for elem in strings:
            dictionary[elem] = integers[idx]
            idx += 1
    return dictionary

