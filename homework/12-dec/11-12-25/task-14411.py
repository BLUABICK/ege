from itertools import *

alph = sorted('СУБЛИМАЦЯ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[-1] != 'Я' and val.count('У') + val.count('И') + val.count('А') + val.count('Я')==2:
        if pos%2!=0:
            print(pos, val)
