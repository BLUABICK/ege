from string import printable as alph
cnt = 0
for x in range(10, 67):
    for y in range(x):
        num1 = 7*67**4 + 3*67**3 + x*67**2 + 1*67**1 + y*67**0
        num2 = 4*x**3 + 9*x**2 + y*x + 6
        num = num1 + num2
        if num:
            cnt+=1
print(cnt)

