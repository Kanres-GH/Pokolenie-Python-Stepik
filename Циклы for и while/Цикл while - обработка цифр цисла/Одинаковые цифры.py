a = int(input())
b = a%10
cnt = 0
while a!=0:
    if a%10!=b:
        cnt+=1
    a//=10
if cnt == 0:
    print('YES')
else:
    print('NO')