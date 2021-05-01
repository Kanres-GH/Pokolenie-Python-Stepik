a = int(input())
if 0<=a<=36:
    if a==0:
        print('зеленый')
    if 1<=a<=10:
        if a%2==0:
            print('черный')
        else:
            print('красный')
    if 11<=a<=18:
        if a%2==0:
            print('красный')
        else:
            print('черный')
    if 19<=a<=28:
        if a%2==0:
            print('черный')
        else:
            print('красный')
    if 29<=a<=36:
        if a%2==0:
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')