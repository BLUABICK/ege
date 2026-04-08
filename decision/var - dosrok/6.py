from turtle import *
tracer(0)
m = 20

rt(315)

for i in range(7):
    fd(12*m)
    rt(45)
    fd(6*m)
    rt(135)

penup()
for x in range(-5, 16):
    for y in range(-5, 20):
        goto(x*m, y*m)
        dot(3, 'red')
print(5*8)
update()
done()
