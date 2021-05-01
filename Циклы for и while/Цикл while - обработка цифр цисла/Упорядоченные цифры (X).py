a = int(input())
flag = False
s = a%10
while a!=0:
    n = a%10
    if n<s:
        flag = True
    else:
        s = n
    a//=10
if flag == True:
    print('NO')
else:
    print('YES')