cnt = 0
for N in range(1, 10000):
    R = f'{N:x}'
    if R.count('b')%2==0:
        R = '1' + R
    else:
        R = R + '1'
    R = str(int(R, 16))
    if len(R)==2:
        cnt+=1
print(cnt)
