from list_function import incert_at

def test_incert_at():   

    ori = [1,2,3,4]
    epected = [1,2,5,3,4]
    result = incert_at(ori, 5, 2)
    assert result == epected

    ori = [1,2,3,4]
    epected = [1,2,5,3,4]
    result = incert_at(ori, 5, 0)
    assert result == epected