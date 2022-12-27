def gen(n):
    a1 = 1
    a2 = 1
    a3 = 1
    v = 2 # 2 ^ k
    s = 0.5 # sum ak / 2^k
    for k in range(4, n):
        yield s
        a4 = a3 + a1
        a1 = a2
        a2 = a3
        a3 = a4
        v += 2
        s += a1 / v
if __name__ == "__main__":
    n = 3
    for item in gen(n + 1):
        print(round(item, 5))


