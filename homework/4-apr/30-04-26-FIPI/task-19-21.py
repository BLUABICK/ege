def f(x, y, s):
    if x + y >= 154:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x + 4, y, s - 1),
         f(x, y + 4, s - 1),
         f(x * 3, y, s - 1),
         f(x, y * 3, s - 1)]
    return any(h) if (s-1)%2==0 else all(h)

print('19)', [x for x in range(1, 142) if f(11, x, 2)])
print('20)', [x for x in range(1, 142) if f(11, x, 3) and not f(11, x, 1)])
print('21)', [x for x in range(1, 142) if f(11, x, 4) and not f(11, x, 2)])
