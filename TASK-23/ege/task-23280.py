def f(a, b):
    if b>a or a==8:
        return 0
    if a == b:
        return 1
    return f(a-1,b)+f(a-4,b)+f(a//3,b)

print(f(19,14)*f(14,2))