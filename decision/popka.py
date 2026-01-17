# print('w x y z')
# for w in 0, 1:
#     for x in 0, 1:
#         for y in 0, 1:
#             for z in 0, 1:
#                 F = (x<=y) and z and not w
#                 if F:
#                     print(w, x, y, z)

# for N in range(1, 100000):
#     R = f'{N:b}'
#     if N%3==0:
#         R = R + R[-3:]
#     else:
#         R = R + f'{N%3*3:b}'
#     R = int(R,2)
#     if R<130:
#         print(N)

# from turtle import *
# screensize(3000, 3000)
# tracer(0)
# m=15
#
# for i in range(2):
#     fd(3*m)
#     rt(90)
#     fd(20*m)
#     rt(90)
# penup()
# bk(8*m)
# rt(90)
# fd(9*m)
# lt(90)
# pendown()
# for i in range(2):
#     fd(16*m)
#     rt(90)
#     fd(8*m)
#     rt(90)
# penup()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x * m, y * m)
#         dot(3, 'red')
#
# print(4*21+17*9-4*9)
# update()
# done()

# def convert(num, sys):
#     res = ''
#     while num:
#         res += str(num % sys)
#         num //= sys
#     return res[::-1]
#
# for x in range(1,3001):
#     y = 9**150+9**30-x
#     R = convert(y, 9)
#     if R.count('0')==122:
#         print(x)
#         break
# from sys import setrecursionlimit
#
# setrecursionlimit(10000000)
# def f(n):
#     if n<10:
#         return n
#     return 3*n + f(n-3)
#
# print((f(6250)+2*f(6244))/f(6238))

# def f(a,b):
#     if b>a or a==13:
#         return 0
#     if a==b:
#         return 1
#     return f(a-1,b) + f(a-2,b) + f(a//3,b)
# m = f(19,6)*f(6,4)
# print(m)

# from re import *

# with open('24_23206.txt') as file:
#     text = file.readline()
#
# text1 = text.replace('0', ' 0').replace('2', ' 2').replace('4', ' 4').replace('6', ' 6').replace('8', ' 8')
#
# text1 = text1.split(' ')
#
# text_2 = []
# for i in text1:
#     if i.count('S')==35:
#         text_2.append(i)
# print(print(len(max(text_2, key=len))))

# text = []
# for i_1 in 'ТЕОРИЯ':
#     for i_2 in 'ТЕОРИЯ':
#         for i_3 in 'ТЕОРИЯ':
#             for i_4 in 'ТЕОРИЯ':
#                 for i_5 in 'ТЕОРИЯ':
#                     for i_6 in 'ТЕОРИЯ':
#                         f = i_1 + i_2 + i_3 + i_4 + i_5 + i_6
#                         text.append(f)
# text.sort()
# cnt = 0
# cnt_1=[]
# for i in text:
#     cnt+=1
#     if i[0] not in 'РТЯ' and i.count('И')>=2:
#         if cnt%2!=0:
#             cnt_1.append(cnt)
# print(cnt_1)

