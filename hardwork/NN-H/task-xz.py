from turtle import *

screensize(3000,3000)
tracer(0)
m = 20

for i in range(2):
    fd(20*m)
    lt(270)
    fd(12*m)
    rt(90)
penup()
fd(9*m)
right(90)
fd(7*m)
lt(90)
pendown()
for i in range(2):
    fd(13*m)
    rt(90)
    fd(6*m)
    rt(90)

penup()
for x in range(-20,30):
    for y in range(-30,20):
        goto(x*m, y*m)
        dot(3,'red')

print(21*13+14*7-12*6)
update()
done()
