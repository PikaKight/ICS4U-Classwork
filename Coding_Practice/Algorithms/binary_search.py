"""
Create a function with the following details:
binary_search(target: int, numbers: int) -> int

It will return the index location, not the found value. 
Return -1 if the value is not in the list.
"""

import os
from typing import List

def binary_search(target: int, numbers: List[int]) -> int:
    
    start = 0
    end = len(numbers) - 1
    while end > -1 and start < len(numbers):
        mid = (start + end) // 2
        if numbers[mid] is target:
            return mid
        elif numbers[mid] < target:
            start = mid + 1
        elif numbers[mid] > target:
            end = mid - 1
    return -1

"""
if __name__ == "__main__":
    os.system("pytest")  # comment out if needed
    main()
"""