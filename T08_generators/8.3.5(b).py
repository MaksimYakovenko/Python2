# p1 = 2
# pk = p(k-1) / (1 + 1 / k ^ 2)

def gen(n):
    s = 2
    for k in range(2, n + 2):
        yield s
        s *= 1 + 1 / k ** 2

if __name__ == "__main__":
    n = 10
    for item in gen(n):
        print(round(item, 2), end = " ")