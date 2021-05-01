from math import sqrt
a = float(input())
b = float(input())
c = float(input())
r1 = float()
r2 = float()
if b**2-4*a*c<0:
    print('Нет корней')
else:
    r1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    r2 = (-b-sqrt(b**2-4*a*c))/(2*a)
    if r1==r2:
        print(r1)
    else:
        print(min(r1,r2))
        print(max(r1,r2))