def f(x, y):
    return (78125 != y + 3 * x) or (a > x) and (a > y)


for a in range(1, 100000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)

