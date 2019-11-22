from binary_search import binary_search


def test_empty_list():
    assert binary_search(5, []) == -1


def test_number_not_found():
    dataset = list(range(100))
    assert binary_search(100, dataset) == -1

    dataset = list(range(3))
    assert binary_search(100, dataset) == -1


def test_found_last_index():
    dataset = list(range(100))
    assert binary_search(99, dataset) == 99


def test_found_middle_index():
    dataset = list(range(3))
    assert binary_search(1, dataset) == 1

    dataset = list(range(100, 200))
    assert binary_search(134, dataset) == 34


def test_found_first_index():
    dataset = list(range(100))
    assert binary_search(0, dataset) == 0