import math
# xN / x(N-1) = x^2 / (2N - 1) / (2N - 2)
def a (x, eps):
    s = x
    prev = 0
    curr = x
    k = 1
    while abs(curr - prev) >= eps:
        prev = curr
        curr *= -x / ((2 * k) * (2 * k + 1))
        k += 1
        s += curr
    return s
x = float(input())
eps = float(input())
print(a(x, eps), math.sinh(x))
