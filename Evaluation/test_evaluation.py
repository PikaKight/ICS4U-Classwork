# from evaluation import *

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

def test_average():
    assert average(1, 2, 3) == 2
    assert average(0,0,0) == 0
    assert average(-5, 10, 0) == 1.6666666666666667
    assert average(-520,-520,-520) == -520

def result_occurance(result: list, specific: str) -> int:
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

def test_result_occurance():
    assert result_occurance(["W", "W", "L", "T", "L"], "W") == 2
    assert result_occurance(["L", "L", "L"], "T") == 0
    assert result_occurance(["W", "T", "W", "W", "L", "W", "T", "T", "L"], "T") == 3

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

def test_occurance_dict():
    assert occurance_dict(["W", "T", "L"]) == {"W": 1, "T": 1, "L": 1}
    assert occurance_dict(["W", "T", "L", "T", "T", "T"]) == {"W": 1, "T": 4, "L": 1}
    assert occurance_dict(["T", "L", "L", "L"]) == {"T": 1, "L": 3}

def occurance_specific(result: dict, specific: str) -> int:
    occurance = 0
    for res in result.keys():
        if specific in res:
            occurance += result[res]
            break
        elif specific not in res:
            occurance = 0
        else:
            continue

    return occurance

def test_occurance_specific():
    assert occurance_specific({"W": 1, "T": 1, "L": 1}, "T") == 1
    assert occurance_specific({"W": 5, "L": 5}, "W") == 5
    assert occurance_specific({"W": 5, "L": 5}, "T") == 0
    assert occurance_specific({"W": 5, "T": 6, "L": 1}, "S") == 0