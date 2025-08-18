# Polygon Rosette
# Auto-generated turtle graphics demo #9
import turtle as t
t.speed(0); t.width(2)
for i in range(36):
    for _ in range(6):
        t.forward(100); t.right(60)
    t.right(10)
    for _ in range(5):
        t.forward(80); t.right(72)
    t.right(10)
t.hideturtle()
t.done()
