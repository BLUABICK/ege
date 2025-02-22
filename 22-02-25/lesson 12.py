# data = 'Hello'
# print(data.split('e'))

# data = 'Hello'
# print(data.replace('l', 'p'))

# data = 'Hello'
# print(data.replace('l', 'p').replace('H', 'G'))

# data = 'Hello'
# print(data.replace(data[2], 'p', 1))

# data = 'Hello'
# print((data[::-1].replace('l', 'p', 1))[::-1])

# data = 'Hello Hello'
# print(data[::-1].replace('l','p', 2).replace('p','l',1).replace('e','o',1)[::-1])

# data = 'Hello Hello'
# old = 'el'
# new = 'po'
# data =data[::-1].replace(old[::-1], new[::-1], 1)[::-1]
# print(data)

# data = 'Иванов Иван Иванович'
# print(data.replace(' ', ','))
# data = ','.join(data.split())
# print(data)

num = '1234'
# def f(num):
#     summ = 0
#     for i in num:
#         summ += int(i)
#     return summ
def f(n):
    return int(num[-1])





data = ['3456', '9876', '23', '9870']
print(len(max(data, key=f)))