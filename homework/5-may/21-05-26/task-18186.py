from re import *
with open('24_18186.txt') as file:
    data = file.readline()
bukvs = r'[BCDFGH][BCDFGH][AE]'
pattern = fr'(?<={bukvs})(([BCDFGH]*[AE]+[BCDFGH]+)|([AE]+[BCDFGH]*[AE]*))(?={bukvs})'

matches = [match.group() for match in finditer(pattern, data)]
print(matches)
print(len(max(matches, key=len))+6)
