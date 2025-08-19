# Double Spiral
# Auto-generated turtle graphics demo #87
import turtle as t
t.speed(0)
d=5
for _ in range(90):
    t.forward(d); t.right(89)
    d += 3
t.left(180)
d=5
for _ in range(90):
    t.forward(d); t.right(89)
    d += 3
t.hideturtle(); t.done()
