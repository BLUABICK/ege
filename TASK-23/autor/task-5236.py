def f(a, b, cnt):
    if a>b or cnt >50:
        return 0
    if a==b:
        return 1
    return f(a+2, b, cnt+1)+f(a*3, b, cnt+1)+f(a*4, b, cnt+1)

print(f(2, 400, 0))