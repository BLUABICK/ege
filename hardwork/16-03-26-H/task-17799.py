from itertools import *

alph = sorted('АРГУМЕНТ')
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if len(set(val))==4 and ord(val[0])<ord(val[1])<ord(val[2])<ord(val[3]):
        print(pos, val)