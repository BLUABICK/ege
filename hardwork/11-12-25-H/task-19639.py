ans = []
for N in range(1, 1000000):
    R = f'{N:b}'
    if R.count('0')%2==0:
        R = '1' + R + '1'
    else:
        R = '10' + R
    R = int(R , 2)
    if R<100:
        ans.append(R)

print(max(ans))