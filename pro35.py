# Checkerboard Outline
# Auto-generated turtle graphics demo #35
import turtle as t
t.speed(0)
size=30
for r in range(8):
    for c in range(8):
        x=-120+c*size; y=120-r*size
        t.penup(); t.goto(x,y); t.pendown()
        for _ in range(4):
            t.forward(size); t.right(90)
t.hideturtle(); t.done()
# Program 35
