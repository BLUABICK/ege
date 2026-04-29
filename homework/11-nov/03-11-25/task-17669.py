from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(4):
    fd(19*m)
    rt(90)
    fd(30*m)
    rt(90)
penup()
fd(2*m)
right(90)
fd(8*m)
left(90)
pendown()
for i in range(4):
    fd(93*m)
    rt(90)
    fd(97*m)
    rt(90)

penup()
for x in range(-50,100):
    for y in range(-150,100):
        goto(x*m, y*m)
        dot(3,'red')

print(17*22)
update()
done()
