def f(start, cnt=0):
    if cnt==8:
        return {start}
    return f(start+1, cnt+1)|f(start+5,cnt+1)|f(start*3, cnt+1)

for i in range(1000, 1025):
    if f(1)==i:
        print(f(1))