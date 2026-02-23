def f(a, b):
    if b>a or a==9 or a ==16:
        return 0
    if a==b:
        return 1
    return f(a-1, b)+f(a-2, b)+ f(a//3, b)

print(f(19, 3))