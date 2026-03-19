from turtle import *
screensize(3000, 3000)
tracer(0)
m= 10

for i in range(4):
    fd(36*m)
    rt(90)
    fd(41*m)
    rt(90)

penup()

rt(90)
fd(20*m)
lt(90)
fd(20*m)

pendown()

for i in range(4):
    fd(25*m)
    rt(90)

penup()

fd(7*m)
lt(90)
fd(7*m)
rt(90)

pendown()

for i in range(7):
    fd(16*m)
    rt(90)
penup()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*m,y*m)
        dot(3,'red')
print(10*10)
update()
done()