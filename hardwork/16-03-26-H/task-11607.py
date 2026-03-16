def f(x):
    return not((x%263==0)<=(x%a==0)) and x%71==0

for a in range(1, 20000)[::-1]:
    if all(not f(x) for x in range(1, 20000)):
        print(a)
        break