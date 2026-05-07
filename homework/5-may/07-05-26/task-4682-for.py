with open('24_4682.txt') as file:
    data = file.readline()

last = ''
last_s = ''
for i in data:
    if i == last_s == 'A' or i == last_s == 'E':
        last +=i
        last_s = i
    elif i == last_s == 'B' or i == last_s == 'C' or i == last_s == 'D':
        last += i
        last_s = i
