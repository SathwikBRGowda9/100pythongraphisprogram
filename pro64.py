# Spiral Dots
# Auto-generated turtle graphics demo #64
import turtle as t, math
t.speed(0)
for i in range(200):
    r = 5 + i*2
    a = i*18
    t.penup(); t.goto(r*math.cos(math.radians(a)), r*math.sin(math.radians(a))); t.pendown()
    t.dot(8)
t.hideturtle(); t.done()
# Program 64
