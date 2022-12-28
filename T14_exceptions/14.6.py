lst = [int(el) for el in input("Введiть елементи списку: ").split()]
def a():
    count = 0
    for i in range(0, 100000):
        try:
            assert i in lst
            count += 1
        except AssertionError:
            continue
    return count
i = a()
print("Кiлькiсть елементiв списку =", i)


def b():
    suma = 0
    for i in range(0, 100000):
        try:
            assert lst[i] in lst
            lst[i] = int(lst[i])
            suma += lst[i]
        except IndexError:
            continue
    return suma
j = b()
print("Сума елементiв спику =", j)


def c():
    m = 0
    for i in range(0, 100000):
        try:
            assert lst[i] in lst
            n = int(lst[i]) / int(lst[i-1])
            if n > m:
                m = n
        except IndexError:
                continue
        except ZeroDivisionError:
                print("У полiдовностi є нульовi елементи")
    return m
k = c()
print("Найбiльше вiдношення =", k)
