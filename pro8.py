# Square Tiling
# Auto-generated turtle graphics demo #8
import turtle as t
t.speed(0); t.width(1)
start_x, start_y = -220, 220
for r in range(9):
    for c in range(9):
        t.penup(); t.goto(start_x+c*50, start_y-r*50); t.pendown()
        for _ in range(4):
            t.forward(40); t.right(90)
t.hideturtle()
t.done()
