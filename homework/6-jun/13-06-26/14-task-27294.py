ans = []
for y in range(1, 9430):
    x = 39**483 + 39**235 - y
    k=0
    while x>0:
        if x%39==0: k+=1
        x//=39
    ans.append(k)
print(max(ans))
