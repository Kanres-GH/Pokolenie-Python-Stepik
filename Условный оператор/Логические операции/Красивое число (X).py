a = int(input())
if (a>=1000 and a<=9999) and(a%7==0 or a%17==0):
    print('YES')
else:
    print('NO')