from typing import List
import random
def merge_sort(num):    
    
    if len(num) == 1:
        return num

    mid = len(num) // 2
    
    s = []
    x = merge_sort(num[:mid])
    y = merge_sort(num[mid:])

    s1 = 0
    s2 = 0

    while s1 < len(x) and s2 < len(y):
        if x[s1] < y[s2]:
            s.append(x[s1])
            s1 += 1
        else:
            s.append(y[s2])
            s2 += 1

    while s1 < len(x):
        s.append(x[s1])
        s1 += 1

    while s2 < len(y):
        s.append(y[s2])
        s2 += 1

    return s


print(merge_sort([6,7,3,8,5,2,4,1]))
print(merge_sort([1, 2, 3, 4, 5]))
print(merge_sort([5, 4, 3, 2, 1, 0]))
print(merge_sort([random.randrange(100) for _ in range(10)]))


"""
def mergesort(numbers: List[int]) -> List[int]:
    # base case
    if len(numbers) == 1:
        return numbers
    
    # find the midpoint
    mid = len(numbers) // 2
    
    # two recursive steps
   
    # mergesort left
    l = mergesort(numbers[:mid])
    # mergesort right
    r = mergesort(numbers[mid:])
   
    # merge the two together
    # loop through both lists with two markers

    s = []
    l_m = 0
    r_m = 0

    while l_m < len(l) and r_m < len(r):
        if l[l_m] < r[r_m]:
            s.append(l[l_m])
            l_m += 1
        else:
            s.append(r[r_m])
            r_m += 1

    # if right value less than left value, add right value to sorted, increase right marker
    # if left value less than right value, add left value to sorted, increase left marker

    # create a while loop to gather the rest of the values from either list

    while r_m < len(r):
        s.append(r[r_m])
        r_m += 1

    while l_m < len(l):
        s.append(l[l_m])
        l_m += 1

    # return the sorted list
        return s
print(mergesort([1, 2, 3, 4, 5]))
print(mergesort([5, 4, 3, 2, 1, 0]))
print(mergesort([random.randrange(100) for _ in range(10)]))
"""