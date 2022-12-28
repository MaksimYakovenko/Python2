from turtle import *
import time

class Clock:
    def __init__(self, hr, mn, sec):
        self._hr = hr
        self._mn = mn
        self._sec = sec

    def draw(self):

        bgcolor("brown")
        setup(width=600, height=600)
        tracer(0)
        hideturtle()
        speed(0)
        pensize(3)

        up()
        goto(0, 210)
        setheading(180)
        color("green")
        pendown()
        circle(210)

        up()
        goto(0, 0)
        setheading(90)

        for _ in range(12):
            fd(190)
            pendown()
            fd(20)
            penup()
            goto(0, 0)
            rt(30)

        hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
        time_set = (hr, mn, sec)

        for hand in hands:
            time_part = time_set[hands.index(hand)]
            angle = (time_part / hand[2]) * 360
            penup()
            goto(0, 0)
            color(hand[0])
            setheading(90)
            rt(angle)
            pendown()
            fd(hand[1])

if __name__ == "__main__":
    home()
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    clock = Clock(hr, mn, sec)
    clock.draw()
    update()
    time.sleep(1)
    mainloop()
