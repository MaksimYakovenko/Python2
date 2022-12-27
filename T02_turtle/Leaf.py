from turtle import *
class Leaf:
    def __init__(self, p1, angle1, radius, extent, angle2, p3):
        self._p1 = p1
        self._angle1 = angle1
        self._radius = radius
        self._extent = extent
        self._angle2 = angle2
        self._p3 = p3

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

        begin_fill()
        goto(self._p1)
        setheading(self._angle1)
        circle(radius, extent)
        setheading(self._angle2)
        circle(radius, extent)
        end_fill()
        goto(self._p3)


        pencolor(oldcolor)
        fillcolor(oldfillcolor)
        width(oldwidth)

if __name__ == "__main__":
    home()
    p1 = (35, 15)
    angle1 = (45)
    radius = -80
    extent = 90
    angle2 = 225
    p3 = (100, 15)
    leaf = Leaf(p1, angle1, radius, extent, angle2, p3)
    leaf.set_outline_color("green")
    leaf.set_fill_color("lime")
    leaf.set_width(2)
    leaf.draw()
    mainloop()
