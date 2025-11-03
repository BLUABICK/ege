text = input()
count = [0] * 128  # [1,2,3,2,1,2,3,4,2,1]
for i in text:
    count[ord(i)] += 1
maxx = 0
for i in count:
    if maxx < i:
        maxx = i
for i in range(128):
    if count[i] == maxx:
        print(chr(i))
        break

