ans =[]
for N in range(151, 10000):
    R = f'{N:x}'
    R = R.replace('a', '1')
    cnt = 0
    for i in range(len(R)):
        if int(R[i],16)%2==0:
            cnt+=1
    if cnt>2:
        R = R +'b'
    else:
        R = 'f' + R
    R = int(R, 16)
    if R > 3500:
        ans.append([R, N])
print(min(ans))
