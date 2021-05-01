import math
sum = 0
cnt = 0
prod = 1
asum = 0
a = int(input())
b = a
while a!=0:
    sum+=int(a)%10
    cnt+=1
    prod*=a%10
    asum = sum/cnt
    a//=10
print(sum)
print(cnt)
print(prod)
print(asum)
print(b//10**(cnt-1))
print(b%10+(b//10**(cnt-1)))