# Simple Koch Snowflake
# Auto-generated turtle graphics demo #10
import turtle as t
t.speed(0); t.width(2)
def koch(n, length):
    if n == 0:
        t.forward(length)
    else:
        koch(n-1, length/3); t.left(60)
        koch(n-1, length/3); t.right(120)
        koch(n-1, length/3); t.left(60)
        koch(n-1, length/3)
t.penup(); t.goto(-150, 80); t.pendown()
for _ in range(3):
    koch(3, 120); t.right(120)
t.hideturtle()
t.done()
