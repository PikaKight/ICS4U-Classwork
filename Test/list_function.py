from typing import List

def incert_at(lis: list, value: int, index: int) -> List:
    
    new_list = [0] * (len(lis) + 1)

    i = 0

    while i < index:
        new_list [i] = lis[i]
        i += 1

    new_list[i] = value
    i += 1

    while i < len(new_list):
        new_list[i] += lis[i - 1]
        i += 1

    return new_list

