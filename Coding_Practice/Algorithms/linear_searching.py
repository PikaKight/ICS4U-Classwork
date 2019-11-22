"""
Search a list of ints for a particular integer. Return the index location, -1 if not found.

Search a list of ints for the last occurrence of a particular integer. -1 if not found.

Search a list of ints for every occurrence of a particular integer. Return a list of every index number. Empty list of not found.

Search a list of strings for words that start with a substring. Return the first occurrence index.

Search a list of strings for words that start with a substring. Return list of all the strings (not the index positions).
"""
from typing import List

def int_search(target: int, numbers: List[int]) -> int:
    for i, num in enumerate(numbers):
        if num is target:
            return i
    return -1

def int_occurrance_search(target:int, numbers: List[int]) -> int:
    numbers = numbers[::-1]
    for i, num in enumerate(numbers):
        if num is target:
            return (len(numbers) - (i + 1))
    return -1

def list_occurrance(target:int, numbers: List[int]) -> List:
    occurrance = []
    for i, num in enumerate(numbers):
        if num is target:
            occurrance.append(i)
    return occurrance
