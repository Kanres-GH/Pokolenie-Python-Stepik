n = int(input())
sum = 0
flag = True
while n!=0:
    last = n % 10
    if last % 2 == 0:
        sum+=last
        flag = True
    else:
        flag = False
    n //= 10
if flag == False:
    print(0)
else:
    print(sum)