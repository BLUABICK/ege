#24 задача егэ я умни
text = input()
cnt = 1
test = []
for i in range(len(text)-1):
    if text[i] in 'ABC':
        if text[i+1] in 'ABC':
            cnt = 1
        else:
            cnt +=1
    else:
        if text[i+1] in '89':
            cnt = 1
        else:
            cnt+=1
    test.append(cnt)
print(test)
print(max(test))



