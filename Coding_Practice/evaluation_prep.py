from typing import *
import math


def sum_of_two(a: int, b: int) -> int:
    """ Adds the two integers togeter 

    Arguments:
        a: the first integer
        b: the second integer
    Return:
        sum of two integer  

    """
    return (a+b)


def sum_of_list(num: List[int]) -> int:
    """ Returns the sum of a list of numbers
    Args:
        List: the list of numbers
    Return: 
        The sum of all the numbers within the list
    """
    total = 0

    for i in num:
        total += i

    return total

def occurence(words: List[str]) -> Dict:
    """ Returns a dictionary with the number of occurence of a word
    Args:
        words: a list words
    Return:
        a dictionary where the key is a word, 
        and the value is the number of times
        it appears in the list 
    """
    occurence = {}

    for word in words:
        if word in occurence.keys():
            occurence[word] += 1
        else:
            occurence[word] = 1

    return occurence
