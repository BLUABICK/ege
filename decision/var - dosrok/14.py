from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

x = 2*2187**567+729**566-2*243**565+81**564-2*27**563-6561
cnt = 0
y = convert2(x, 27)
for i in y:
    if int(i, 27)%2==0 and int(i, 27)>9:
        cnt+=1
print(cnt)