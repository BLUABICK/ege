from fnmatch import *

for i in range(171, 10**8+1, 171):
    if fnmatch(str(i), '1*23??56'):
        print(i, i//171)