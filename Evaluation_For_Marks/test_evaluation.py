from evaluation import *

def test_average():
    assert average(1, 2, 3) == 2
    assert average(0,0,0) == 0
    assert average(-5, 10, 0) == 1.6666666666666667
    assert average(-520,-520,-520) == -520

def test_result_occurance():
    assert result_occurrence(["W", "W", "L", "T", "L"], "W") == 2
    assert result_occurrence(["L", "L", "L"], "T") == 0
    assert result_occurrence(["W", "T", "W", "W", "L", "W", "T", "T", "L"], "T") == 3

def test_occurance_dict():
    assert occurrence_dict(["W", "T", "L"]) == {"W": 1, "T": 1, "L": 1}
    assert occurrence_dict(["W", "T", "L", "T", "T", "T"]) == {"W": 1, "T": 4, "L": 1}
    assert occurrence_dict(["T", "L", "L", "L"]) == {"T": 1, "L": 3}

def test_occurance_specific():
    assert occurrence_specific({"W": 1, "T": 1, "L": 1}, "T") == 1
    assert occurrence_specific({"W": 5, "L": 5}, "W") == 5
    assert occurrence_specific({"W": 5, "L": 5}, "T") == 0
    assert occurrence_specific({"W": 5, "T": 6, "L": 1}, "S") == 0
