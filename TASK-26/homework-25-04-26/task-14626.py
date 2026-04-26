with open(r'..\files\26_14626.txt') as file:
    N = int(file.readline())
    K, M = map(int, file.readline().split())
    nums = list(map(int, file.readline().split()))
    weights = sorted(int(i) for i in file)

caves = {}
