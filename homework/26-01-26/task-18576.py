print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = not(w <= (x == y)) and (z <= x)
                if F:
                    print(x, y, z, w)
