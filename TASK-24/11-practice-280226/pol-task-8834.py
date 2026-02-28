from re import finditer
with open(r'..\files\24-371.txt') as file:
    data = file.readline()

pattern = r'(A[B-Z ]*){98}\.'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)))