mx = -10000000000
s = 0
flag = True
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        flag = False
        if x > mx:
            mx = x
if flag == True:
    print('NO')
else:
    print(s)
    print(mx)