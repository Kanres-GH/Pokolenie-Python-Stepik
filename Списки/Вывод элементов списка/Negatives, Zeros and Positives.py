n = int(input())
l = list()
neg = list()
z = list()
pos = list()
for i in range(n):
    s = int(input())
    l.append(s)
    if l[i]<0:
        neg.append(s)
    if l[i]>0:
        pos.append(s)
    if l[i]==0:
        z.append(s)
print(*neg,sep='\n')
print(*z,sep='\n')
print(*pos,sep='\n')