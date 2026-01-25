from turtle import *

screensize(3000,3000)
tracer(0)
m = 20

for i in range(13):
    fd(13*m)
    rt(90)
    fd(5*m)
penup()
right(90)
fd(7*m)
left(90)
fd(10*m)
pendown()
for i in range(23):
    fd(8*m)
    lt(90)
    fd(11*m)
    lt(90)

penup()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m, y*m)
        dot(3,'red')

print(18*18+8*11-7*3)
update()
done()
