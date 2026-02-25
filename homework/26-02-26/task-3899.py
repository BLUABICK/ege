def f(a, b):
    if a==b:
        return 1
    if a<10:
        return 0
    return f(a//10+a%10, b) or f((a//10)*(a%10), b)
cnt = 0

for i in range(10, 100):
    if f(i, 8):
        cnt+=1
    print(cnt)