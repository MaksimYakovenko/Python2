

def gen(n):
    d1 = a + b
    d2 = a ** 2 + a * b + b ** 2
    for _ in range(1, n + 1):
        yield d1
        d3 = d1 * d2 - a * b * d1
        d1 = d2
        d2 = d3



if __name__ == "__main__":
    a = 0
    b = -1
    n = 2
    for item in gen(n):
        print(item)
