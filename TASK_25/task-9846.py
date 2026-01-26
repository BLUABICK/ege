from fnmatch import fnmatch

for N in range(2025, 10**8+1, 2025):
    if fnmatch(str(N), '12*34?5'):
        print(N, N//2025)