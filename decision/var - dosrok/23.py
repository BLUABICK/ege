def f(a, b):
    if a>b or a==7:return 0
    if a==b:
        return 1
    return f(a+1, b)+f(a+3,b)+ f(a*2,b)

print(f(2, 15)* f(15, 25))