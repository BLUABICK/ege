def f(x):
    return ((not str(x)[0]=='2') and str(x)[0]=='4') <=(x>a-20)


for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break