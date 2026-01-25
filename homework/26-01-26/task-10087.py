ans = []
for N in range(1, 1000):
    R = f'{N:b}'
    if N%3==0:
        R = R + R[-3:]
    else:
        R = R + f'{(N%3)*3:b}'
    R = int(R, 2)
    if R >151:
       ans.append(R)
print(min(ans))