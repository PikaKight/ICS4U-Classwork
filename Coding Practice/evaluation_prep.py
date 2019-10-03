from typing import *
import math


def sum_of_two(a: int, b: int) -> Int:
    """ Function that takes two integers and returns the sum 

    Arguments:
        a: the first integer
        b: the second integer
    Return:
        sum of a and b  

    """
    return (a+b)


def sum_of_list(List: list) -> Int:
    """ Returns the sum of a list of numbers
    Args:
        List: the list of numbers
    Return: 
    """
    total = 0
    for i in List:
        total += List[i]
    return total
