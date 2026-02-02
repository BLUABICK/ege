print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = not(w<=z) or (x<=y) or not x
                if not F:
                    print(w, x, y, z)