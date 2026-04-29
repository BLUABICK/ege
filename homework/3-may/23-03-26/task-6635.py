ans =set()
def f(a, s):
    if s ==13:
        ans.add(a)
    else:
        f(a-3,s+1)
        f(a*(-3), s+1)
f(333, 0)
print(len([i for i in ans if i<0]))
