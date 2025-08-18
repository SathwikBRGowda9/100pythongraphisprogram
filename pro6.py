# Circle Spiral
# Auto-generated turtle graphics demo #6
import turtle as t, math
t.speed(0); t.width(2)
for i in range(200):
    r = 2 + i*0.6
    angle = i*20
    t.penup()
    t.goto(r*math.cos(math.radians(angle)), r*math.sin(math.radians(angle)))
    t.pendown()
    t.circle(12)
t.hideturtle()
t.done()
# Program 6
