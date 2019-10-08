from typing import *

def average(a: float, b: float, c: float) -> float:
    """ Takes the average of 3 float numbers
    Args:
        a: Float number 1
        b: Float number 2
        c: Float number 3
    returns:
        average: The average of the 3 float numbers
    """
    average = (a + b + c) / 3

    return average 

def result_occurance(result: List[str], specific: str) -> int:
    """ Finds the number of occurance a specific result appears in a list of results.
    Args:
        result: A list of wins, loss, and ties
        specific: The specific result a user is looking for
    Return:
        occurance: The number of occurances the specific result has in a given list  
    """  
    occurance = 0

    for res in result:
        if res in specific:
            occurance += 1
        else:
            continue
    return occurance

def occurance_dict(result: list) -> dict:
    """ Takes a list of results and turns it into a dict
        that has the number of occurance for each specific results
    Args:
        result: A list of wins, loss and ties
    Returns:
        occurance: A dictionary that has the results as the keys, and the occurance as the values
    """
    occurance = {}

    for res in result:
        occurance[res] = 0
    
    for res in result:
        for key in occurance.keys():
            if res in key:
                occurance[res] += 1
            else:
                continue
    
    return occurance 

def occurance_specific(result:dict, specific: str) -> int:
    """ Takes a sorted inventory dictionary of results and their respected occurances and returns a specific result's occurance
    Args:
        result: a dictionary of wins, lose, and ties and their respected occurances
        specific: a specific result that is being seachered for
    Returns:
        The number of occurances the specific result has
    """
    for res in result.keys():
        if specific in res:
            return result[res]
        else:
            continue
