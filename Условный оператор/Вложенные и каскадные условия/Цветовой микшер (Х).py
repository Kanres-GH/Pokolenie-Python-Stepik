a = input()
b = input()
if (a=='красный' or b=='красный') and (a=='синий' or b=='синий'):
    print('фиолетовый')
elif (a=='красный' or b=='красный') and (a=='желтый' or b=='желтый'):
    print('оранжевый')
elif (a=='синий' or b=='синий') and (a=='желтый' or b=='желтый'):
    print('зеленый')
elif a==b=='красный':
    print(a)
elif a==b=='синий':
    print(a)
elif a==b=='желтый':
    print(a)
else:
    print('ошибка цвета')