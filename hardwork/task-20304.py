from turtle import *

screensize(3000,3000)
tracer(0)
m = 20

for i in range(9):
    fd(30*m)
    rt(90)
    fd(12*m)
    rt(90)
penup()
lt(270)
fd(5*m)
lt(90)
pendown()
for i in range(2):
    fd(24*m)
    rt(90)
    fd(28*m)
    rt(90)

penup()
for x in range(-30,35):
    for y in range(-30,35):
        goto(x*m, y*m)
        dot(3,'red')

print((7*7+24*24)**0.5)
update()
done()
