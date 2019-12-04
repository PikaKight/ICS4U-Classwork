from typing import List
def bubble_sort(num: List[int]):
    i = 0 
    n = len(num) - 1
    while i <= n - 1:
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

print(bubble_sort([5, 7, 1, 9, 20, 2, 6, 3]))
print(bubble_sort([1, 0, 1]))
