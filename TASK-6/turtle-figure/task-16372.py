from turtle import *

screensize(3000, 3000)
tracer(False)
m = 10

for i in range(2):
    fd(23 * m)
    lt(90)
    bk(27 * m)
    lt(90)
penup()
bk(5 * m)
rt(90)
fd(11 * m)
lt(90)
pendown()

for i in range(2):
    fd(26 * m)
    rt(90)
    fd(32 * m)
    rt(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')

print(27*33+24*28-22*17)
update()
done()