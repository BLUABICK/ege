from fnmatch import *

for i in range(9874, 10**10+1, 9874):
     if fnmatch(str(i), '89*6?7?9?') and i%9874==0:
         print(i, i//9874)
