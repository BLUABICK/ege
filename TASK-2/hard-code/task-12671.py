print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = not (x==(w and not z)) and (y==(x and not w))
                if F:
                    print(w, x, y, z)
