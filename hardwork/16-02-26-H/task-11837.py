def f(x, y):
    return (x**2+y**2>1024-x) or (y<-2*x+a)


for a in range(1, 10000):
    if all(f(x, y) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break