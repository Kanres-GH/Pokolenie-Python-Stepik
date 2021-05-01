a = input()
n = '1234567890'
flag = False
for i in range(len(a)):
    if a[i] in n:
        flag = True
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')