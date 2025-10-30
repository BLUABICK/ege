from turtle import *

screensize(3000,3000)
tracer(0)
m = 20

for i in range(2):
    fd(13*m)
    rt(90)
    fd(20*m)
    rt(90)
penup()
fd(8*m)
right(90)
bk(3*m)
left(90)
pendown()
for i in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)

penup()
for x in range(-20,30):
    for y in range(-30,30):
        goto(x*m, y*m)
        dot(3,'red')

print(14*21+9*17-36)
update()
done()
