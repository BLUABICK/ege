from turtle import *
screensize(3000,3000)
tracer(0)
m= 20

for i in range(3):
    fd(27*m)
    rt(90)
    fd(12*m)
    rt(90)
penup()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
pendown()

for i in range(34):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
penup()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*m,y*m)
        dot(3,'red')
print(28*13+84*78-7*24)
update()
done()