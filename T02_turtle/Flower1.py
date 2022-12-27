from turtle import *
from Stem import Stem
from Leaf import Leaf
from Petal import Petal
class Flower1:

    _count = 0

    @staticmethod
    def get_count():
        return Flower1._count

    def __init__(self, stem, leaf, petal):
        self._stem = Stem
        self._leaf = Leaf
        self._petal = Petal

        Flower1._count += 1

if __name__ == "__main__":
    home()
    p = (0, 300)
    angle = (90)
    r = 50
    k = 7
    p1 = (35, 15)
    angle1 = (45)
    radius = -80
    extent = 90
    angle2 = 225
    p3 = (100, 15)

    stem = Stem(p, angle)
    stem.set_outline_color("brown")
    stem.set_width(2)
    stem.draw()

    petal = Petal(r, k)
    petal.set_outline_color("red")
    petal.set_fill_color("pink")
    petal.set_width(3)
    petal.draw()

    leaf = Leaf(p1, angle1, radius, extent, angle2, p3)
    leaf.set_outline_color("green")
    leaf.set_fill_color("lime")
    leaf.set_width(2)
    leaf.draw()

    flower = Flower1(Stem, Leaf, Petal)
    flower.draw(stem.draw(), petal.draw(), leaf.draw())
    print(Flower1.get_count())

    mainloop()


