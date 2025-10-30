from turtle import *

screensize(3000,3000)
tracer(0)
m = 20

for i in range(2):
    fd(10*m)
    rt(90)
    fd(18*m)
    rt(90)
penup()
fd(5*m)
right(90)
fd(7*m)
left(90)
pendown()
for i in range(2):
    fd(10*m)
    rt(90)
    fd(7*m)
    rt(90)

penup()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m, y*m)
        dot(3,'red')

print(19*11+11*8-6*8)
update()
done()
