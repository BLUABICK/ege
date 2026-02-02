print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                F = (not a and not b) or (b == c) or d
                if not F:
                    print(a, b, c, d)