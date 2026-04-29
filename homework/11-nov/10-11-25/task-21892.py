from turtle import *

screensize(3000, 3000)
tracer(0)

m = 20

rt(90)
for i in range(7):
    rt(45)
    fd(11*m)
    rt(45)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
print(8*8+7*7)
update()
done()