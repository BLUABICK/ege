def fact(num):
    d = []
    while num%2 ==0:
        d+=[2]
        num//=2
    i = 3
    while i*i <num+1:
        while num%i==0:
            d+=[i]
            num//=i
        i+=2
    if num>2:
        d+=[num]
    return d

cnt = 0
for N in range(3600001, 10**10):
    M = fact(N)
    if len(M)==3 and all('3' in str(m) and '5' in str(m) for m in M):
        print(N, M)
        cnt+=1
        if cnt==5:
            break