n = int(input())
s = n
m7 = 1
sum5 = 0
cnt3 = 0
cnt2 = 0
cnt05 = 0
cntl = 0
while n!=0:
    last = n%10
    if last == 3:
        cnt3+=1
    if last==s%10:
        cntl+=1
    if last%2==0:
        cnt2+=1
    if last>5:
        sum5+=last
    if last>7:
        m7*=last
    if last==0 or last==5:
        cnt05+=1
    n//=10
print(cnt3)
print(cntl)
print(cnt2)
print(sum5)
print(m7)
print(cnt05)