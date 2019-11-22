from Coding_Practice.Algorithms.linear_searching import *

def test_int_search():
    assert int_search(1, []) == -1
    assert int_search(1, [1 , 5 , 2]) == 0
    assert int_search(5, [5]) == 0
    assert int_search(5, [1, 2, 3, 4, 5]) == 4
    assert int_search(5, [2, 5, 2]) == 1
    assert int_search(5, [6, 5, 5]) == 1

def test_int_occurrance_search():
    assert int_occurrance_search(1, []) == -1
    assert int_occurrance_search(1, [1 , 5 , 2, 1]) == 3
    assert int_occurrance_search(5, [5, 4, 85, 4]) == 0
    assert int_occurrance_search(4, [1, 2, 3, 4, 5]) == 3
    assert int_occurrance_search(2, [2, 5, 2]) == 2
    assert int_occurrance_search(5, [6, 5, 5]) == 2

def test_list_occurrance():
    assert list_occurrance(1, []) == []
    assert list_occurrance(1, [1 , 5 , 2, 1]) == [0, 3]
    assert list_occurrance(5, [5, 4, 85, 4]) == [0]
    assert list_occurrance(4, [1, 4, 3, 4, 5]) == [1,3]
    assert list_occurrance(2, [2, 5, 2]) == [0, 2]
    assert list_occurrance(5, [6, 5, 5]) == [1,2]