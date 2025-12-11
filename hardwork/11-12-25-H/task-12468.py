from string import printable as alph
ans = []
for x in alph[:19]:
    num_1 = int(f'78{x}79643', 19)
    num_2 = int(f'25{x}43', 19)
    num_3 = int(f'63{x}5', 19)
    num = num_1 + num_2 + num_3
    if num%18==0:
        ans.append([x, num//18])
print(min(ans))