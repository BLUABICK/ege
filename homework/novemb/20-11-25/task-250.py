ans =[]
for N in range(41):
    if f'{N:b}'[-4:]=='1011':
        ans.append(N)
print(max(ans))