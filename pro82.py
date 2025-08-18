# Diamond Grid
# Auto-generated turtle graphics demo #82
import turtle as t
t.speed(0)
start_x, start_y = -220, 220
for r in range(8):
    for c in range(8):
        t.penup(); t.goto(start_x+c*55, start_y-r*55); t.pendown()
        for _ in range(4):
            t.forward(40); t.right(90)
        t.right(45)
t.hideturtle(); t.done()
# Program 82
