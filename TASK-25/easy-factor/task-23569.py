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
    if len(d)==2 and str(d[0]).count('6')==str(d[1]).count('6')==1:
        return max(d)
    return 0

cnt = 0
for i in range(6_086_055, 10**20):
    M = fact(i)
    if M:
        print(i, M)
        cnt +=1
        if cnt==5:
            break
