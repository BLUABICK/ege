with open(r"26_23383.txt") as file:
    N = int(file.readline())
    check_points = {}
    for i in file:
        runner, check_point = map(int, i.split())
        if check_point in check_points:
            check_points[check_point].add(runner)
        else:
            check_points[check_point] = {runner}

commonest_check_point = []
for check_point in check_points:
    cnt = 1
    max_cnt = 0
    sorted_check_points = sorted(check_points[check_point])
    for runners in zip(sorted_check_points, sorted_check_points[1:]):
        if runners[1] - runners[0] == 1:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    max_cnt = max(max_cnt, cnt)
    commonest_check_point.append([max_cnt, check_point])

print(max(commonest_check_point, key=lambda x: (x[0], -x[1])))




