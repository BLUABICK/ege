from itertools import *

# permutations - формирует всевозможные перестановки элементов коллекции
alph_1 = '123'
for val_1 in permutations(alph_1):
    val = ''.join(val_1)
    print(val)

# product - формирует всевозможные комбинации определённой длинны
alph_2 = '123'
for val_2 in product(alph_2, repeat=3):
    val = ''.join(val_2)
    print(val)

# enumerate - нумерует элементы последовательности начиная от start
alph_3 = '123'
res = enumerate(alph_3, start=1)
print(*res)
