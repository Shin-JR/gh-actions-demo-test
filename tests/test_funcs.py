from main.funcs import division, sum_2_digits, sum_multiple


def test_sum_2_digits():
    assert sum_2_digits(0, 0) == 0
    assert sum_2_digits(0, 1) == 1
    assert sum_2_digits(-2, 5) == 3
    assert sum_2_digits(999999, 123456) == 1123455


def test_sum_multiple():
    assert sum_multiple(1, 2, 3, 4) == 10
    assert sum_multiple(1, 2, 3, 4, 5, 6) == 21
    assert sum_multiple(1, 2, 3, 4, 5, 6, 7) == 28
    assert sum_multiple(1, 2, 3, 4, 5, 6, 7, 8) == 36


def test_division():
    assert division(4, 2) == 2
    assert division(6, 3) == 2
    assert division(18, 3) == 6
    assert division(1, 0) == 1
