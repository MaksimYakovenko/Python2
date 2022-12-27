import math


def b (x, eps):
    x0 = x / 3
    while abs(x0 ** 3 - x) >= eps:
        x0 = (2 * x0 + x / x0 ** 2) / 3
    return x0

x = float(input())
eps = float(input())
print(b(x, eps), math.sqrt(x))
