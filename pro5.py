# Regular Polygons Gallery
# Auto-generated turtle graphics demo #5
import turtle as t
t.speed(0)
t.penup(); t.goto(-250,0); t.pendown()
for sides in range(3, 9):
    for _ in range(sides):
        t.forward(60); t.right(360/sides)
    t.penup(); t.forward(90); t.pendown()
t.hideturtle()
t.done()
# Program 5
