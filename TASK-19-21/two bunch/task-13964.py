from math import ceil
def f(x, y, s):
    if x + y <= 108:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x - 2, y, s - 1),
         f(x, y -2, s - 1),
         f(ceil(x/2), y, s - 1),
         f(x, ceil(y/2), s - 1)]
    return any(h) if (s-1)%2==0 else all(h)

print('19)', [x for x in range(49, 1000) if f(60, x, 2)])
print('20)', [x for x in range(49, 1000) if f(60, x, 3) and not f(60, x, 1)])
print('21)', [x for x in range(49, 1000) if f(60, x, 4) and not f(60, x, 2)])