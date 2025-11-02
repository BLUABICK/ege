from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
penup()
fd(1*m)
right(90)
fd(5*m)
left(90)
pendown()
for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)

penup()
for x in range(-50,100):
    for y in range(-150,100):
        goto(x*m, y*m)
        dot(3,'red')

print(22+22)
update()
done()
