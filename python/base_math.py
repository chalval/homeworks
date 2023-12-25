




        res *= item
        res += item
        res -= item
        res /= item
    for item in args:
    for item in args:
    for item in args[_CONTINUATION:]:
    for item in args[_CONTINUATION:]:
    print(f'{add(2, 4) = }')
    print(f'{add(2, 4, 6, 8) = }')
    print(f'{div(-100, 5, -2) = }')
    print(f'{mul(2, 2, 2, 2, 2) = }')
    print(f'{sub(10, 2) = }')
    res = _START_MULT
    res = _START_SUM
    res = args[_BEGINNING]
    res = args[_BEGINNING]
    return res
    return res
    return res
    return res
"""
"""Four basic mathematical operations.
Addition, subtraction, multiplication and division as functions.
_BEGINNING = 0
_CONTINUATION = 1
_START_MULT = 1
_START_SUM = 0
def add(*args):
def div(*args):
def mul(*args):
def sub(*args):
if __name__ == '__main__':
