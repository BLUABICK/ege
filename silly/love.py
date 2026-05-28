from math import *
from turtle import *
def xt(t):
 return 13*sin(t)**3
def yt(t):
 return 13*cos(t)-5* cos(2*t)-2*cos(3*t)-cos(4*t)
speed(1500)
colormode(255)
Screen().bgcolor(0,0,0)
for i in range(255):
 goto((xt(i)*20, yt(i)*20))
 pencolor((255-i)%255,10%255,((255+i)//2)%255)
 goto(0,0)
hideturtle()
update()
mainloop()
