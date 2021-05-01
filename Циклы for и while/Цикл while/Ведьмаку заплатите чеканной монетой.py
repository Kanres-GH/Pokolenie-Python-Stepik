cnt = 0
a = int(input())
while a>=25:
    a-=25
    cnt+=1
while a>=10:
    a-=10
    cnt+=1
while a>=5:
    a-=5
    cnt+=1
while a>=1:
    a-=1
    cnt+=1
print(cnt)