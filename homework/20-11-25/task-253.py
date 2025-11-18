from string import digits, ascii_lowercase


def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


for N in range(2, 37):
    if convert2(41, N)[-1] == '2' and convert2(131, N)[-1] == '1':
        print(N)
