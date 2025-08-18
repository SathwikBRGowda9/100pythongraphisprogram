# Circle Grid
# Auto-generated turtle graphics demo #61
import turtle as t
t.speed(0)
start_x, start_y = -220, 220
for r in range(7):
    for c in range(7):
        t.penup(); t.goto(start_x+c*70, start_y-r*70-35); t.pendown()
        t.circle(35)
t.hideturtle(); t.done()
