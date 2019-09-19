def kangaroo(input):
    if not isinstance(input, str):
        raise Exception('Invalid input')
    return kangaroo_calc(*map(int, input.split()))


def kangaroo_calc(x1, v1, x2, v2):
    return x1 == x2 if v1 == v2 else ((x2-x1)/(v1-v2)) % 1 == 0


