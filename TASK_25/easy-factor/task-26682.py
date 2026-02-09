def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True



def fact(num): #170->85->
    d = [] # 2
    while num%2 ==0:
        d+=[2]
        num//=2
    i = 3 # 5 7
    while i*i <num+1:  #85 -> 28 -> 5
        while num%i==0:
            d+=[i]
            num//=i
        i+=2
    if num>2:
        d+=[num]

    if len(d)==9:


        def f(num):
            d = set()
            for i in range(2, int(num ** .5) + 1):
                if num % i == 0:
                    d |= {i, num // i}

            if len(d) > 1:
                return min(d) + max(d)
            return 0


cnt = 0
for i in range(6_086_055, 10**20):
    M = fact(i)
    if M:
        print(i, M)
        cnt +=1
        if cnt==5:
            break
