cnt = 0
a = int(input())
b = a
while a!=0:
    a//=10
    cnt+=1
print((b//10**(cnt-2))%10)