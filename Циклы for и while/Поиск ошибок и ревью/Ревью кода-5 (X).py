n = int(input())
s = n
cnt = 0
while n > 0:
    last = n%10
    cnt+=1
    n //= 10
print(s//10**(cnt-1))