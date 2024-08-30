def sum_2_digits(a: int | float, b: int | float) -> int | float:
    return a + b


def sum_multiple(*args: int | float) -> int | float:
    return sum(args)


def division(dividend: int | float, divisor: int | float) -> float:
    if divisor == 0:
        raise ZeroDivisionError
    return dividend / divisor
