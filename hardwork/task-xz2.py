from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

fd(30*m)
lt(60)
fd(24*m)
rt(240)

fd(54*m)
lt(120)
fd(24*m)
lt(60)

penup()
fd(30*m)
right(90)
fd(20*m)
lt(90)
pendown()
for i in range(17):
    fd(6*m)
    lt(90)
    fd(80*m)
    lt(90)

penup()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m, y*m)
        dot(3,'red')

print(21**2+12**2)
print(11**2+6**2)
print(24-12+21+6+10)
update()
done()
