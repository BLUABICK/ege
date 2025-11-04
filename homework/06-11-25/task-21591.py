from turtle import *

screensize(3000,3000)
tracer(0)
m = 10
rt(270)
for i in range(2):
    fd(8*m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3*m)
    rt(240)
rt(240)
for i in range(2):
    fd(14*m)
    rt(120)



penup()
for x in range(-50,70):
    for y in range(-50,50):
        goto(x*m, y*m)
        dot(3,'red')

print(14*12/2)
update()
done()