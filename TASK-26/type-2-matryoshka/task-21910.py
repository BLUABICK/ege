with open('../files/26_21910.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file.readlines()]

boxes = sorted(boxes, reverse=True)
last_box =boxes[0]
cnt = 1
for box in boxes:
    if last_box-box>=9:
        cnt+=1
        last_box = box

print(cnt, last_box)