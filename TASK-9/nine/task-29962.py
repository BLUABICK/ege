with open('../files/9_29962') as file:
    data = [list(map(int, i.split())) for i in file.readlines()]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        pov = [i for i in line if line.count(i)!=1]
        non_pov = [i for i in line if line.count(i)==1]
        if sum(non_pov)/len(non_pov)>pov[0]:
            print(pos)

