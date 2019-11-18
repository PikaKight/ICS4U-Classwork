"""
Search a list of ints for a particular integer. Return the index location, -1 if not found.

Search a list of ints for the last occurance of a particular integer. -1 if not found.

Search a list of ints for every occurance of a particular integer. Return a list of every index number. Empty list of not found.

Search a list of strings for words that start with a substring. Return the first occurance index.

Search a list of strings for words that start with a substring. Return list of all the strings (not the index positions).
"""
from typing import List

def int_search(target: int, numbers: List[int]) -> int:
    for num in numbers:
        if num is target:
            return num
    return -1

