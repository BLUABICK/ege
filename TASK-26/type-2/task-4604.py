with open('../files/26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file.readlines()]

boxes = sorted(boxes, reverse=True)

box = boxes[0]
cnt = 1
for i in range(len(boxes)):
    if box-boxes[i]>=3:
        cnt+=1
        box = boxes[i]

print(cnt, box)




