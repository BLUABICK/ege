def f(a, b, c=''):
    if a > b:
        return 0
    if a == b and c[-1]!='C':
        return 1
    return f(a + 2, b, c + 'A') + f(a + 5, b, c + 'B') + f(a**2, b, c + 'C')

print(f(4, 36))
