from evaluation_prep import *

def test_sum_of_two():
    assert sum_of_two(5,6) == 11
    assert sum_of_two(1,0) == 1
    assert sum_of_two(1000, -1000) == 0

def test_sum_of_list():
    assert sum_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert sum_of_list([0,0,0,0,0,0,0,1]) == 1

def test_occurence():
    assert occurence(["Hello", "Hello", "It's", "ME", "ME"]) == {"Hello": 2, "It's": 1, "ME": 2}
    assert occurence(["YES", "I", "AM", "Yes", "Oui", "oui", "Beguitte"]) == {"YES": 1, "I": 1, "AM": 1, "Yes": 1, "Oui": 1, "oui": 1, "Beguitte": 1}