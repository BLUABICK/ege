from fnmatch import *
def f(num):
    d = set()
    for i in range(1, int(num**.5)+1):
        if num%i==0:
            d |= {i, num//i}
    if len(d)>=30:
        return sum(d)
    return 0

for i in range(53, 10**7, 53):
    if fnmatch(str(i), '*2?2*') and str(i)== str(i)[::-1] and f(i):
        print(i, f(i))

