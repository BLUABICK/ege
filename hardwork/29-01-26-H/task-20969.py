from fnmatch import fnmatch

for N in range(154682, 10**11+1,154682):
    if fnmatch(str(N), '*192?3*68'):
        print(N, N//154682)