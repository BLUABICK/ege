with open('26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    res = []
    for i in file:
        res.append(list(map(int, i.split())))

res.sort(key=lambda arr: (-(arr[1]+arr[2]+arr[3]+arr[4]), -arr[4], arr[0]))
print(res)
# for i in range(len(res)):
#     if res[i]