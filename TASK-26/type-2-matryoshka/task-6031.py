with open('../files/26_6031.txt') as file:
    N = int(file.readline())
    rings = [int(i) for i in file.readlines()]

rings = sorted(rings, reverse=True)
cnt = 1
big_ring = rings[0]
for ring in rings:
    if big_ring-ring>=6:
        cnt+=1
        big_ring= ring
print(cnt, big_ring)