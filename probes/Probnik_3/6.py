from turtle import *
screensize(3000, 3000)
tracer(0)
m=15

for i in range(4):
    fd(10*m)
    rt(270)

penup()
fd(3*m)
rt(270)
fd(5*m)
rt(90)
pendown()

for i in range(2):
    fd(10*m)
    rt(270)
    fd(12*m)
    rt(270)
penup()

for x in range(0, 20):
    for y in range(0, 20):
        goto(x*m, y*m)
        dot(3, 'red')
print(11*11+11*13-6*8)
update()
done()
