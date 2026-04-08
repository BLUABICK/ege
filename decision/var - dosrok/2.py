from itertools import product, permutations

def f(x, y, z, w):
    return (w==z) or not(y<=w) or not x

for i in product((0, 1), repeat=5):
    table = [
        (0, 0, 1, i[0]),
        (i[1], 1, 1, i[2]),
        (0, i[3], i[4], 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')

print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = (w==z) or not(y<=w) or not x
                if not F:
                    print(w, x, y, z)