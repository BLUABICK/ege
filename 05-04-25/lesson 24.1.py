with open('../02-04-25/26_7602.txt') as file:
    N = int(file.readline())
    M = int(file.readline())
    boxes = [list(map(int, i.split())) for i in file]
print(boxes)