import math
def gen(x, log1p):
    s = 2 * x
    a = 1
    while abs(x) < 1:
        yield s
        a = (1 + x) / (1 - x)
        s += a
if __name__ == '__main__':
    x = 3
    log1p = 0.01
    for item in gen(x, log1p):
        print(item)

    print(math.log1p(x))




