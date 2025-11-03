# text = input()
# res = ''
# for i in text:
#     if 'a' <= i <= 'z':
#        res += chr(ord(i)-32)
#     else:
#         res += i
# print(res)

# text = input()
# res = ''
# frst = text[0]
# if 'A' <= frst <= 'Z':
#     res += frst
# else:
#     res += chr(ord(frst) - 32)
#
# for i in range(1, len(text)):
#     if 'A' <= text[i] <= 'Z':
#         res += chr(ord(text[i])+32)
#     else:
#         res += text[i]
# print(res)

st1 = input()
st2 = input()
l = len(st2)
print(st1[-l:]==st2)