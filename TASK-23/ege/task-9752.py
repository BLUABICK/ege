def f(a, b):
    if a>b or a==17:
        return 0
    if a==b:
        return 1
    return f(a+2,b)+f(a+3,b)+f(a*2,b)

print(f(3,10)*f(10,25))