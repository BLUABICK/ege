with open('26_4604.txt') as file:
    N = int(file.readline())
    boxes = []
    for i in file.readlines():
        boxes.append(int(i))
boxes.sort(reverse=True)
print(boxes)
cnt = 1
last_box = boxes[0]
for box in range(len(boxes)):
    if boxes[box] <= last_box - 3:
        cnt+=1
        last_take_num = boxes[box]
print(cnt, last_box)

