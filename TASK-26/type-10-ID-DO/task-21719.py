with open('../files/26_21719.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file.readlines()]

students = {}

for i in data:
    if i[0] in students:
        students[i[0]] |= {i[1]}
    else:
        students[i[0]] = {i[1]}

for i in students:
    students[i]=sorted(students[i])

ans = []
for student in students.items():
    cnt = 1
    for i in range(len(student[1])-1):
        if student[1][i+1]-student[1][i]==2:
            cnt+=1
            ans.append([student[0], cnt])
        else:
            cnt=1


print(*max(ans, key=lambda x:(x[1], -x[0])))


