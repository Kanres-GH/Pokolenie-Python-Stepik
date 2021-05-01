a = int(input())
if a%2==0:
    if 2<=a<=5:
        print('NO')
    elif 6<=a<=20:
        print('YES')
    elif a>20:
        print('NO')
else:
    print('YES')