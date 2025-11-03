from turtle import *

screensize(3000, 3000)
tracer(0)
m = 20

rt(45)
for i in range(10):
    rt(45)
    bk(203*m)
    rt(45)

penup()
bk(40*m)
rt(45)
pendown()


for i in range(2):
    fd(20*m)
    lt(90)


penup()

print(202*202-19*19)
update()
done()