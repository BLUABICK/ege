from traceback import print_tb

with open('26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = {}
    for i in file:
        sailor = list(map(int, i.split()))
        sailors[sailor[0]] = (sum(sailor[1:-1]), sailor[-1])
sailors_2 = sorted(sailors, key=lambda x: (sailors[x], -x), reverse=True)
last_sailor_ID = 0
cnt_half_point = 0
half_point=0
last_passed = sailors_2[S-1]
first_not_passed = sailors_2[S]
if sailors[last_passed][0] == sailors[first_not_passed][0]:
    half_point = sailors[last_passed][0]
    for id in sailors_2:
        if sailors[id][0] == half_point:
            cnt_half_point +=1
        elif sailors[id][0] > half_point:
            last_sailor_ID = id
print(last_sailor_ID, cnt_half_point)




