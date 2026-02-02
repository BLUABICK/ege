def f(x):
    return (not(x%10==5%10) and x%10==4%10)<= (x>a-11)


for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
