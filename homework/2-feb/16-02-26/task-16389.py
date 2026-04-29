from fnmatch import fnmatch

for N in range(98591, 10**10+1, 98591):
    if fnmatch(str(N), '5?2*3?3?'):
        print(N, N//98591)