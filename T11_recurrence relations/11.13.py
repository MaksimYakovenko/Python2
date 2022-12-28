def a(n):
    d1 = 2
    d2 = 3
    for i in range(n - 1):
        d3 = 2 * d2 - 1 * d1
        d1 = d2
        d2 = d3
    return d1


if name == 'main':
    n = int(input())

    print(a(n))
