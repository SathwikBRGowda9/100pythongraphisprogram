# Heart Outline
# Auto-generated turtle graphics demo #36
import turtle as t, math
t.speed(0); t.width(3)
t.penup(); t.goto(0,-120); t.pendown()
for a in range(361):
    r=200
    x = 16*math.sin(math.radians(a))**3
    y = 13*math.cos(math.radians(a)) - 5*math.cos(math.radians(2*a)) - 2*math.cos(math.radians(3*a)) - math.cos(math.radians(4*a))
    t.goto(x*10, y*10-120)
t.hideturtle(); t.done()
