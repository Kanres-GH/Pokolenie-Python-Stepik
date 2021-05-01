a = input()
cntp = 0
cnts = 0
for i in range(len(a)):
    if a[i] == '+':
        cntp+=1
    if a[i] == '*':
        cnts+=1
print('Символ + встречается', cntp, 'раз')
print('Символ * встречается', cnts, 'раз')