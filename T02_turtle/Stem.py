from turtle import *
class Stem:
    def __init__(self, p, angle):
        self._p = p
        self._angle = angle

        self._outline = "black"
        self._width = 1

    def set_outline_color(self, color):
        self._outline = color

    def set_width(self, _width):
        self._width = _width

    def draw(self):
        oldcolor = pencolor()
        oldwidth = width()

        pencolor(self._outline)
        width(self._width)

        goto(self._p)
        setheading(self._angle)

        pencolor(oldcolor)
        width(oldwidth)

if __name__ == "__main__":
    home()
    p = (0, 300)
    angle = (90)
    stem = Stem(p, angle)
    stem.set_outline_color("brown")
    stem.set_width(2)
    stem.draw()
    mainloop()