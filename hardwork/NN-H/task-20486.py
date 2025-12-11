ans = []
for N in range(4, 10000):
     R = f'{N:b}'
     if N%2==0:
         R = R + R[:3]
     else:
         R = '1' + R + '01'
     R = int(R, 2)
     if R > 600:
        ans.append(R)
print(min(ans))

