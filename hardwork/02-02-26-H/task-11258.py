from fnmatch import *

for i in range(8387, 10**9+1, 8387):
     if fnmatch(str(i), '*75?122*'):
         print(i, i//8387)