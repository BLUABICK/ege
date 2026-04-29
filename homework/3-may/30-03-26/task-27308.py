def f(a, b):
    if a<b and a!=38:
        return 0
    if a==b:
        return 1
    return f(a-3,b)+f(a-5,b)+f(a//3,b)

def f1(a, b):
    if a<b and a!=18:
        return 0
    if a==b:
        return 1
    return f(a-3,b)+f(a-5,b)+f(a//3,b)

def f2(a, b):
    if a<b:
        return 0
    if a==b:
        return 1
    return f(a-3,b)+f(a-5,b)+f(a//3,b)

print(f(80,18)*f(18,3)+f1(80,38)*f1(38,3)-f2(80,38)*f2(38,18)*f(18,3))


