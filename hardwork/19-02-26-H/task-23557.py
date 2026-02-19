from math import *

for L in range(1, 10 ** 8):
    N = 562
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 45877*I > 49*2**20:
        print(L)
        break
