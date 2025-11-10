from turtle import  *
screensize(3000,3000)
tracer(0)
m = 10

for i in range(2):
    fd(21*m)
    rt(90)
    fd(27*m)
    rt(90)
penup()
fd(9*m)
rt(90)
fd(10*m)
lt(90)
pendown()
for i in range(2):
    fd(86*m)
    rt(90)
    fd(47*m)
    rt(90)

penup()
for x in range(-50,70):
    for y in range(-50,50):
        goto(x*m, y*m)
        dot(3,'red')

print(13*18)
update()
done()
