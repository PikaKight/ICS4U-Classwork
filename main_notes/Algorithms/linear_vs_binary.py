import timeit
from typing import List

def linear_search(target: int, data: List) -> int:
    for i, num in enumerate(data):
        if num == target:
            return i

    return -1

def binary_search(target:int, data: List) -> int:
    
    start = 0

    end = len(data) - 1

    while start <= end:

        mid = (start + end) // 2

        if data[mid] is target:
            return mid

        elif data[mid] < target:
            start = mid + 1
        
        else:
            end = mid - 1

    return -1

DATASET_SIZE = 10**11
NUMBER_OF_CALLS = 10000
SEARCH_TARGET = DATASET_SIZE // 2

dataset = range(DATASET_SIZE)
result_b = timeit.timeit(
    "binary_search(SEARCH_TARGET, dataset)",
    setup="import random",
    number=NUMBER_OF_CALLS,
    globals=globals())

print(result_b)