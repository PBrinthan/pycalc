def compute(expression):
    """Perform simple arithmetic encoded in an input string.

    Examples:
        '1 + 2' -> 3
        '1 - 2' -> -1
    """
    num0, operator, num1 = expression.split(' ')
    num0, num1 = int(num0), int(num1)

    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        return None

def test_compute():
    """Basic tests for compute function."""
    assert compute("1 + 2") == 3
    assert compute("5 - 3") == 2
    assert compute("2 * 4") == 8
    assert compute("8 / 2") == 4
