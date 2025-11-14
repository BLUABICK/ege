def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for N in range(1, 10000):
    R = convert(N, 9)
    for j in range(4):
        if R.count('5') == R.count('7'):
            R = R + R[-1]
        else:
            cnt = []
            for i in R:
                cnt.append(R.count(i))
                maxx = max(cnt)
                ind = cnt.index(maxx)
                R = R + R[ind]
    R = convert2(int(R,9), 16)
    if 'BAC' in R:
        print(N)
# Борис Олегович, я сошел с ума пока ето решал и не вышло, ну нафек


