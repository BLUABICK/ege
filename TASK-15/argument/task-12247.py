def f(x):
    return (x&a == 0) or not (x&37==0) or not (x&12==0)

for a in range(0, 1000):
    if all(f(x) for x in range(0, 1000)):
        print(a)