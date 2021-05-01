flag = False
for i in range(10):
    a = int(input())
    if a%2==0:
        flag = True
    else:
        flag = False
        break
if flag == True:
    print('YES')
else:
    print('NO')