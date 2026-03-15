with open(r'../files/26_16335.txt') as file:
    N = int(file.readline())
    crusts = [int(i) for i in file]

crusts = sorted(crusts, reverse=True)

all_crust = [crusts[0]]
last_crust = 0
for crust in crusts:
    if all_crust[-1] - crust >= 4:
        last_crust = crust
        all_crust.append(crust)
print(len(all_crust), last_crust)
