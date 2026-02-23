def f(a,b):
    if b>a:
        return 0
    if a == b:
        return 1
    return f(a-1, b) + f(a-3, b) + f(a//3, b)

print(f(22,2))