from turtle import *

screensize(3000, 3000)
tracer(0)
m = 20

for i in range(2):
    fd(5*m)
    lt(90)
    bk(13*m)
    lt(90)

penup()
bk(10*m)
rt(90)
fd(9*m)
lt(90)
pendown()


for i in range(2):
    fd(11*m)
    rt(90)
    fd(7*m)
    rt(90)

penup()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m, y*m)
        dot(3,'red')

print(14*6+8*12-5*2)
update()
done()