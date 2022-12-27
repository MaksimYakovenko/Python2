from turtle import *
class Petal:
    def __init__(self, r, k):
        self._r = r
        self._k = k

        self._outline = "black"
        self._fill = "black"
        self._width = 1

    def set_outline_color(self, color):
        self._outline = color

    def set_fill_color(self, color):
        self._fill = color

    def set_width(self, _width):
        self._width = _width

    def draw(self):
        oldcolor = pencolor()
        oldfillcolor = fillcolor()
        oldwidth = width()

        pencolor(self._outline)
        fillcolor(self._fill)
        width(self._width)

        for i in range(k):
            begin_fill()
            circle(r)
            end_fill()
            left(360 / k)
            continue

        pencolor(oldcolor)
        fillcolor(oldfillcolor)
        width(oldwidth)

if __name__ == "__main__":
    home()
    r = 50
    k=7
    petal = Petal(r, k)
    petal.set_outline_color("red")
    petal.set_fill_color("pink")
    petal.set_width(3)
    petal.draw()
    mainloop()

