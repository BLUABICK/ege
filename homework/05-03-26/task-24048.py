def convert(num, x):
    val = 0
    for i in num:
        val = val * x + int(i, 36)
    return val


for p in range(33, 100):
    num1 = convert('KOT', p)
    num2 = convert('GOLODNI', p)
    num3 = convert('MEEOW', p)
    num4 = convert('100', p)
    if num1 + num2 == num3 * num4 - 20194023088:
        print(convert('PURR', p))
