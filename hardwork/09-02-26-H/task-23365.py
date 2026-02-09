from turtle import *
screensize(3000, 3000)
tracer(0)
m = 10

for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)

penup()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
pendown()

for i in range(3):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 20):
        goto(x*m, y*m)
        dot(3,'red')
print(39*48+29*18-12*18)
update()
done()