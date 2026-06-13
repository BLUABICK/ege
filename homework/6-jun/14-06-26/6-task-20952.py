from turtle import *
screensize(3000, 3000)
tracer(0)
m = 35
for i in range(5):
    fd(6*m)
    rt(90)
    fd(3*m)
    rt(90)

penup()
fd(4*m)
rt(90)
fd(2*m)
rt(90)
pendown()

for i in range(8):
    fd(8*m)
    rt(90)
    fd(5*m)
    rt(90)

penup()
fd(4*m)
rt(90)
fd(2*m)
lt(90)
pendown()

for i in range(5):
    fd(5*m)
    lt(90)

penup()
for x in range(-10, 15):
    for y in range(-10, 10):
        goto(x*m, y*m)
        dot(3, 'red')
print(18+25+40-16)
update()
done()