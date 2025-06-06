# Физмат школа
# оценка по физике (2 ... 5)
# оценка по математике (2 ... 5)
# средний балл (2.0 ... 5.0)
# амбиции (1, 0)
# возраст (7, 17)
# рост (100, 200)
# вес (40, 200)
# iq (0, 200)
students = [
    [4, 5, 4.7, 1, 15, 199, 150, 10], # (4.7, 5, 4, 1) -> 2
    [2, 2, 2.0, 0, 7, 100, 40, 1], # (2.0, 2, 2, 0) -> 8
    [5, 5, 5.0, 0, 11, 130, 140, 150], # (5.0, 5, 5, 0) -> 1
    [4, 4, 4.1, 1, 16, 190, 40, 30], # (4.1, 4, 4, 1) -> 4
    [3, 4, 3.7, 1, 12, 190, 50, 45], # (3.7, 4, 3, 1) -> 5
    [2, 5, 4.5, 0, 17, 140, 50, 20], # (4.5, 5, 2, 0) -> 3
    [3, 3, 3.0, 1, 16, 120, 40, 60], # (3.0, 3, 3, 1) -> 7
    [2, 3, 3.4, 0, 17, 170, 60, 130]  # (3.4, 3, 2, 0) -> 6
]

# средний балл, iq, вес, оценка по физике, возраст, оценка по математике, рост, амбиции

students.sort(key=lambda arr: (arr[2], arr[7], arr[6], arr[0], arr[4], arr[1], arr[5], arr[3]), reverse=True)
for i in students:
    print(i)