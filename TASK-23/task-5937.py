def f(a, b, cnt):
    if a>b or cnt >15:
        return 0
    if a==b:
        return 1
    return f(a+2, b, cnt+(a+3)%2)+f(a+3, b, cnt+(a+4)%2)+f(a*2+1, b, cnt+(a*2+1+1)%2)

print(f(1, 55, 0))