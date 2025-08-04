from timeit import timeit

with open('26_21719.txt') as file:
    N = int(file.readline())
    tasks = []
    for i in file:
        tasks.append(list(map(int, i.split())))


def f_ART_1(N, tasks):
    tasks.sort(reverse=True)
    cnt = 1
    res = []
    for i in range(len(tasks) - 1):
        if tasks[i][0] == tasks[i + 1][0]:
            if tasks[i][1] != tasks[i + 1][1]:
                if tasks[i][1] - tasks[i + 1][1] == 2:
                    cnt += 1
                else:
                    res.append([tasks[i][0], cnt])
                    cnt = 1
        else:
            res.append([tasks[i][0], cnt])
            cnt = 1
    (res.sort(key=lambda x: (x[1], -x[0])))


(print(timeit('f_ART_1', globals=globals(), number=1_000_000_000)))