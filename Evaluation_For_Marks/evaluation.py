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
 
def result_occurrence (result: List[str], specific: str) -> int:
    """ Finds the number of occurrences  a specific result appears in a list of results.
    Args:
        result: A list of wins, loss, and ties
        specific: The specific result a user is looking for
    Return:
        occurrence : The number of occurrences the specific result has in a given list  
    """  
    occurrence  = 0
 
    for res in result:
        if res in specific:
            occurrence += 1
        else:
            continue
 
    return occurrence
 
def occurrence_dict(result: list) -> dict:
    """ Takes a list of results and turns it into a dict
        that has the number of occurrences for each specific results
    Args:
        result: A list of wins, losses and ties
    Returns:
        occurrence: A dictionary that has the results as the keys, and the occurrences as the values
    """
    occurrence = {}
 
    for res in result:
        occurrence[res] = 0
    
    for res in result:
        for key in occurrence.keys():
            if res in key:
                occurrence[res] += 1
            else:
                continue
    
    return occurrence 
 
def occurrence_specific(result:dict, specific: str) -> int:
    """ Takes a sorted inventory dictionary of results and their respected occurrences and returns a specific result's occurrence
    Args:
        result: a dictionary of wins, losses, and ties and their respective occurrences
        specific: a specific result that is being searched for
    Returns:
        The number of occurrences the specific result has
    """
 
    occurrence = 0
 
    for res in result.keys():
        if specific in res:
            occurrence += result[res]
            break
        elif specific not in res:
            occurrence = 0
        else:
            continue
 
    return occurrence