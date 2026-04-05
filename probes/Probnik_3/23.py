def f(a, b):
    if a<b or a==7:
        return 0
    if a==b:
        return 1
    return f(a-1,b)+f(a-4,b)+f(a//3,b)

print(f(19,13)*f(13,2))