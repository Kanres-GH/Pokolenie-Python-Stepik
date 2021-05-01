n = int(input())
l = list()
for i in range(n):
    s = int(input())
    l.append(s)
l.remove(max(l))
l.remove(min(l))
print(*l,sep='\n')