# Rose Curve 6 Petals
# Auto-generated turtle graphics demo #62
import turtle as t, math
t.speed(0)
t.penup()
for a in range(0, 361*4, 2):
    k=3
    r = 150*math.sin(math.radians(k*a))
    x = r*math.cos(math.radians(a))
    y = r*math.sin(math.radians(a))
    t.goto(x,y); t.pendown()
t.hideturtle(); t.done()
