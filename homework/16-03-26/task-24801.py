def f(a, b, n):
    if a == b:
        return 1
    elif a > b or a == n:
        return 0
    else:
        return f(a + 1, b, n) + f(a + 2, b, n) + f(a + 4, b, n) + f(a + 8, b, n)

x = f(16, 24, 32) * f(24, 48, 32)
y = f(16, 32, 24) * f(32, 48, 24)
print(x + y)