import math
from 3.3.1 import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Triangle'

    def dim(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = 'Rectangle'

    def dim(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.name = 'Trapeze'

        coef = []
        coef.append(a)
        coef.append(b)
        coef.append(c)
        coef.append(d)

        for i in range(len(coef) - 1):
            for j in range(len(coef) - 1 - i):
                if coef[j] > coef[j + 1]:
                    coef[j], coef[j + 1] = coef[j + 1], coef[j]

        a, b, c, d = coef
        self.a = d
        self.b = c
        self.c = b
        self.d = a

    def dim(self):
        return 2

    def perimeter(self):
        p = self.a + self.b + self.c + self.d
        return p

    def square(self):
        if self.a > self.b and self.c > self.d:
            S = (self.a + self.b) / 2
            s = (self.c ** 2 - (((self.a - self.b) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.a - self.b)))) ** 0.5
            return S * s
        else:
            p2 = self.perimeter() / 2
            s = ((p2 - self.a) * (p2 - self.b) * (p2 - self.c) * (p2 - self.d)) ** 0.5
            return s


class Parallelogram(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Parallelogram'

    def dim(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.c


class Circle(Figure):
    def __init__(self, a):
        self.a = a
        self.name = 'Circle'

    def dim(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.a

    def square(self):
        return math.pi * (self.a ** 2)




