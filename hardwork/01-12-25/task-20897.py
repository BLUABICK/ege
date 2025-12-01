from turtle import *
screensize(3000,3000)
tracer(0)
m = 10

for i in range(9):
    fd(27*m)
    rt(90)
    fd(30*m)
    rt(90)
penup()
fd(3*m)
rt(90)
fd(6*m)
lt(90)
pendown()
for i in range(9):
    fd(77*m)
    rt(90)
    fd(66*m)
    rt(90)

penup()
for x in range(-50,100):
    for y in range(-50, 100):
        goto(x*m, y*m)
        dot(3, 'red')
print(24*4)
update()
done()

