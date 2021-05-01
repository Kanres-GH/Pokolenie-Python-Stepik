n = int(input())
l = list()
cnt = 0
for i in range(n):
    s = int(input())
    cnt+=1
    l.append(s)
for j in range(n):
    sm2 = sum(l[j:j+2])
    l.append(sm2)
del l[:len(l)//2]
del l[-1]
print(l)