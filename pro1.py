# Concentric Circles
# Auto-generated turtle graphics demo #1
import turtle as t
t.bgcolor("white")
t.speed(0)
t.width(2)
for r in range(20, 240, 10):
    t.penup(); t.goto(0, -r); t.pendown()
    t.circle(r)
t.hideturtle()
t.done()
# Program 1
