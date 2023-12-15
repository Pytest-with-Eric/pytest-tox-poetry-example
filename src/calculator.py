def addition(a: int | float, b: int | float) -> int | float:
    return a + b


def subtraction(a: int | float, b: int | float) -> int | float:
    return a - b


def multiplication(a: int | float, b: int | float) -> int | float:
    return a * b


def division(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


# if __name__ == "__main__":
#     print(addition(2, 3))
#     print(subtraction(2, 3))
#     print(multiplication(2, 3))
#     print(division(2, 3))
    # print(division(2, 0))
