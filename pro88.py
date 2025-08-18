# Triangle Grid
# Auto-generated turtle graphics demo #88
import turtle as t
t.speed(0)
start_x, start_y = -220, 220
for r in range(7):
    for c in range(7):
        t.penup(); t.goto(start_x+c*65, start_y-r*65); t.pendown()
        for _ in range(3):
            t.forward(50); t.right(120)
t.hideturtle(); t.done()
# Program 88
