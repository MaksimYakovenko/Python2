from Flower1 import Flower1
from turtle import *
import random

def random_point(xmax, ymax):
    x = random.randint(-xmax, xmax)
    y = random.randint(-ymax, ymax)
    return x, y

if __name__ == "__main__":
    home()
    xmax, ymax = screensize ()

    while Flower1.get_count() < 5:
        p = random_point(xmax, ymax)
        angle = (90)
        k = 7
        r = 50
        p1 = random_point(xmax, ymax)
        angle1 = (45)
        radius = -80
        extent = 90
        angle2 = 225
        p3 = random_point(xmax, ymax)

    mainloop()