from turtle import *
class Flower:

    _count = 0

    @staticmethod
    def get_count():
        return Flower._count

    def __init__(self, p, angle, r, k, p0, p1, angle1, radius, extent, angle2, p3):
        self._p = p
        self._angle = angle
        self._r = r
        self._k = k
        self._p0 = p0
        self._p1 = p1
        self._angle1 = angle1
        self._radius = radius
        self._extent = extent
        self._angle2 = angle2
        self._p3 = p3

        Flower._count += 1

    def draw(self):
        setup(800, 850)

        goto(self._p)
        setheading(self._angle)

        for i in range(k):
            begin_fill()
            circle(r)
            end_fill()
            left(360 / k)
            continue

        penup()
        goto(self._p0)
        pendown()
        goto(self._p1)
        setheading(self._angle1)
        circle(radius, extent)
        setheading(self._angle2)
        circle(radius, extent)
        goto(self._p3)

if __name__ == "__main__":
    home()
    p = (0, 300)
    angle = (90)
    r = 50
    k = 7
    p0 = (0, 10)
    p1 = (35, 15)
    angle1 = (45)
    radius = -80
    extent = 90
    angle2 = 225
    p3 = (100, 15)
    flower = Flower(p, angle, r, k, p0, p1, angle1, radius, extent, angle2, p3)
    flower.draw()
    print(Flower.get_count())
    mainloop()
