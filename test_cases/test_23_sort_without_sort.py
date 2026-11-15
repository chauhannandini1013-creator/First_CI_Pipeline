import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_normal_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty_list():
    assert bubble_sort([]) == []


def test_negative_numbers():
    assert bubble_sort([3, -1, 2]) == [-1, 2, 3]


def test_duplicates():
    assert bubble_sort([2, 2, 1]) == [1, 2, 2]


def test_original_not_changed():
    original = [3, 1, 2]
    bubble_sort(original)
    assert original == [3, 1, 2]