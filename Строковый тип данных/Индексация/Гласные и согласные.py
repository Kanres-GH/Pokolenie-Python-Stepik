gl = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
sogl = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
a = input()
cntgl = 0
cntsogl = 0
for i in range(len(a)):
    if a[i] in gl:
        cntgl+=1
    if a[i] in sogl:
        cntsogl+=1
print('Количество гласных букв равно', cntgl)
print('Количество согласных букв равно', cntsogl)