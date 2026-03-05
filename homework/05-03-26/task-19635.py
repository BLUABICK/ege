from math import ceil

def f(x, y, s):
    if x + y <= 100:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x - 3, y - 3, s - 1),
         f(x//2, y, s - 1),
         f(x, y//2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else any(h)


print('19)', [x for x in range(53, 500) if f(48, x, 2)]) # 52
print('20)', [x for x in range(53, 500) if f(48, x, 3) and not f(48, x, 1)])
print('21)', [x for x in range(53, 500) if f(48, x, 4) and not f(48, x, 2)])
