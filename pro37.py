# Star Grid
# Auto-generated turtle graphics demo #37
import turtle as t
t.speed(0)
def star(s):
    for _ in range(5):
        t.forward(s); t.right(144)
start_x, start_y = -220, 220
for r in range(5):
    for c in range(5):
        t.penup(); t.goto(start_x+c*90, start_y-r*90); t.pendown()
        star(60)
t.hideturtle(); t.done()
# Program 37
