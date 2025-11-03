from turtle import *
screensize(3000,3000)
tracer(False)
m = 10

for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)

penup()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
pendown()

for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3,'red')
print(29*19+31*8-15*8)
update()
done()