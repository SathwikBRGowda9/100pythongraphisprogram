# Approx Fibonacci Spiral
# Auto-generated turtle graphics demo #81
import turtle as t
t.speed(0)
sizes=[10,10]
for _ in range(10):
    sizes.append(sizes[-1]+sizes[-2])
for i,s in enumerate(sizes):
    t.circle(s,90)
t.hideturtle(); t.done()
# Program 81
