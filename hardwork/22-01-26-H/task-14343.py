def convert(num, sys):
    res = ''
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]

x = 5*343**2031 + 4*49**2149 - 3*7**111 + 7**222
print(sum(map(int, convert(x, 7))))