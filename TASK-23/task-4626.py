def f(a, b):
    if b>a:
        return 0
    if a==b:
        return 1
    return f(a-2, b) + f(a//2, b)

print(f(28, 10)*f(10,1))