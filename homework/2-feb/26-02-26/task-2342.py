def f(a, b):
    if a>b:
        return 0
    if a==b:
        return 1
    if a<b and a%10!=9:
        return f(a+1, b)+f(a+11, b)
    if a<b and a%10==9:
        return f(a+1, b)+f(a+10, b)

print(f(25,51))
