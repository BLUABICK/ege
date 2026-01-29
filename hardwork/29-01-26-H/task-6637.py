from fnmatch import fnmatch

for N in range(3052, 10**10+1, 3052):
    if fnmatch(str(N), '1?2139*4'):
        print(N, N//3052)
