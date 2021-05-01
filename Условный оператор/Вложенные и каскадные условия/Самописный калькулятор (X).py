a = int(input())
b = int(input())
s = input()
if s=='+':
    print(a+b)
elif s=='-':
    print(a-b)
elif s=='*':
    print(a*b)
elif s=='/':
    if b==0:
        print('На ноль делить нельзя!')
    else:
        print(a/b)
elif s!='+' or s!='-' or s!='/' or s!='*':
    print('Неверная операция')