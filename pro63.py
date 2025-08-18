# Lissajous Curve
# Auto-generated turtle graphics demo #63
import turtle as t, math
t.speed(0)
t.penup()
A,B,a,b,delta = 200,150,3,2,math.pi/3
for tt in [i/200 for i in range(0, 2000)]:
    x = A*math.sin(a*tt + delta)
    y = B*math.sin(b*tt)
    t.goto(x,y); t.pendown()
t.hideturtle(); t.done()
# Program 63
