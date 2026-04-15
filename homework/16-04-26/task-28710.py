def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fact(num):
    d = []
    while num%2 ==0:
        d+=[2]
        num//=2
    i = 3
    while i*i <num+1:
        while num%i==0 and is_prime(num%i):
            d+=[i]
            num//=i
        i+=2
    if num>2 and is_prime(num):
        d+=[num]
    if len(d)==3 and 5 in d and 3 in d:
        return max(d)
    return 0
cnt = 0
for N in range(3600000, 10**10):
    M = fact(N)
    if M:
        print(N, M)
        cnt+=1
        if cnt==5:
            break