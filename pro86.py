# Starry Dots Spiral
# Auto-generated turtle graphics demo #86
import turtle as t, math
t.speed(0)
for i in range(160):
    r=3*i; a=11*i
    t.penup(); t.goto(r*math.cos(math.radians(a)), r*math.sin(math.radians(a))); t.pendown()
    t.dot(6)
t.hideturtle(); t.done()
# Program 86
