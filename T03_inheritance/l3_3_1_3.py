import math
from 3.3.1_2 import Triangle, Rectangle, Circle
from 3.3.1 import Figure


class TriangularPyramid(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = 'Triangular Pyramid'

    def dim(self):
        return 3

    def squareSurface(self):
        return 0.5 * self.a * 3 * self.b

    def squareBase(self):
        p = (self.a * 3) / 2
        return (p * ((p - self.a) ** 3)) ** 0.5

    def square(self):
        return self.squareSurface() + self.squareBase()

    def height(self):
        return self.b

    def _volume(self):
        return 1/3 * (self.squareBase() * self.b)


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d
        self.name = 'Triangular Prism'

    def dim(self):
        return 3

    def perimeter(self):
        return self.d * 3 + 2 * super().perimeter()

    def squareSurface(self):
        return super().perimeter() * self.d

    def squareBase(self):
        return super().square()

    def square(self):
        return 2 * self.squareBase() + self.squareSurface()

    def height(self):
        return self.d

    def _volume(self):
        return self.squareBase() * self.height()


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
        self.name = 'Quadrangular Pyramid'

    def dim(self):
        return 3

    def squareSurface(self):
        return super().perimeter() * self.c

    def squareBase(self):
        return super().square()

    def square(self):
        return self.squareBase() + self.squareSurface()

    def height(self):
        return self.c

    def _volume(self):
        return 1/3 * (self.squareBase() * self.c)


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
        self.name = 'Rectangular Parallelepiped'

    def dim(self):
        return 3

    def perimeter(self):
        return (self.a + self.b + self.c) * 4

    def squareSurface(self):
        return 2 * (self.a + self.b) * self.c

    def squareBase(self):
        return self.a * self.b

    def square(self):
        return 2 * self.squareBase() + self.squareSurface()

    def height(self):
        return self.c

    def _volume(self):
        return self.a * self.b * self.c


class Cone(Circle):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
        self.name = 'Cone'

    def dim(self):
        return 3

    def squareSurface(self):
        line = math.sqrt(self.a ** 2 + self.b ** 2)
        return math.pi * line * self.a

    def squareBase(self):
        return super().square()

    def square(self):
        return self.squareBase() + self.squareSurface()

    def height(self):
        return self.b

    def _volume(self):
        return 1/3 * (super().square() * self.b)


class Ball(Figure):
    def __init__(self, a):
        self.a = a
        self.name = 'Ball'

    def dim(self):
        return 3

    def square(self):
        return 4 * math.pi * (self.a ** 2)

    def height(self):
        return 2 * self.a

    def _volume(self):
        return 4/3 * (math.pi * self.a ** 3)


if __name__ == '__main__':
    q = QuadrangularPyramid(14, 18, 22)
    print(q._volume())
