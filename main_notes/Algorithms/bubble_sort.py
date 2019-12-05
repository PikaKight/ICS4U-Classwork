from typing import List
import random
def bubble_sort(num: List[int]):
    i = 0 
    n = len(num) - 1 #5
    while i <= n - 1: #4
        if i == n -1:
            if num[i] > num[i + 1]:
                x = num[i+1]
                num[i + 1] = num[i]
                num[i] = x
                i = 0
                n -= 1
            else:
                return num
        elif num[i] > num[i + 1]:
            x = num[i+1]
            num[i + 1] = num[i]
            num[i] = x
            i += 1
        else:
            i += 1
    return num
    
print(bubble_sort([5, 7, 1, 9, 20, 2, 6, 3]))
print(bubble_sort([1, 0, 1]))
print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1, 0]))
print(bubble_sort([random.randrange(100) for _ in range(10)]))