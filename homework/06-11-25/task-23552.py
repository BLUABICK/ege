from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(5):
    fd(37*m)
    rt(90)
    fd(44*m)
    rt(90)
penup()
bk(18*m)
right(90)
fd(29*m)
left(90)
pendown()
for i in range(5):
    fd(31*m)
    rt(90)
    fd(35*m)
    rt(90)

penup()
for x in range(-50,70):
    for y in range(-50,50):
        goto(x*m, y*m)
        dot(3,'red')

print(14*16)
update()
done()
