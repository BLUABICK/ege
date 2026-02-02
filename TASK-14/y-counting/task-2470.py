from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

cnt = 0
for i in range(1000):
    if len(convert2(i, 5))==4 and len(convert2(i, 3))==5 and convert2(i, 16)[-1] == 'd':
        cnt +=1
print(cnt)