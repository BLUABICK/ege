from turtle import *

screensize(3000,3000)
tracer(0)
m = 10
for i in range(4):
    fd(30*m)
    rt(90)
    fd(48*m)
    rt(90)
penup()
fd(27*m)
right(90)
fd(24*m)
lt(90)
pendown()
for i in range(4):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)

penup()
for x in range(-50,70):
    for y in range(-50,50):
        goto(x*m, y*m)
        dot(3,'red')

print((18+3)*2)
#x=30
update()
done()