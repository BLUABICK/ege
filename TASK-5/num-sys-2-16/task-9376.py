R1 =[]
for N in range(1, 100000):
    R = f'{N:b}'
    if N%3==0:
        R = R + R[-3:]
    else:
        R = R + bin((N%3)*3)[2:]
    R = int(R,2)
    if R <=170:
        R1.append(R)
print(max(R1))