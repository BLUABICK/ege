from turtle import *
screensize(3000, 3000)
tracer(False)
m=20

rt(30)
for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*m,y*m)
        dot(3,'red')

update()
done()