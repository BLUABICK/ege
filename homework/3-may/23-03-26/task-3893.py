def f(x):
    return (a%25==0) and (((x%24==0) and (x%75==0))<=(x%a==0))
cnt = 0
for a in range(1, 100000):
    if all(f(x) for x in range(-1000000000, 1000000000)):
        cnt+=1
print(cnt)