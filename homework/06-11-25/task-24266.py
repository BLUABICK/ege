from turtle import *

screensize(3000,3000)
tracer(0)
m = 10
for x1 in range(100):
    for i in range(4):
        fd(x1*m)
        rt(90)
        fd(48*m)
        rt(90)
penup()
fd(27*m)
right(90)
fd(24*m)
rt(90)
pendown()
for i in range(4):
    fd(29*m)
    rt(90)
    fd(18*m)
    rt(90)

penup()
for x in range(-50,70):
    for y in range(-50,50):
        goto(x*m, y*m)
        dot(3,'red')

#Блин я хз как тут сделать я не пойму

update()
done()