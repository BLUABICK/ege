from math import *

for N in range(1, 10 ** 8):
    L = 2783
    i = ceil(log2(N))  # bit
    I = ceil(L * i / 8)  # byte
    if 3_845_627 * I >= 11 * 2 ** 30:
        print(N)
        break