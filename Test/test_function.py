import math

def test_sum():
    assert sum([1, 1, 1]) == 3
    assert sum([1] * 10000) == 10000
    assert sum([9]) == 9

def test_f_strings():
    a = 5
    assert f"hello {a}" == "hello 5"