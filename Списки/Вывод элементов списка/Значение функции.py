n = int(input())
l = list()
l2 = list()
for i in range(n):
    s = int(input())
    l.append(s)
    f = (l[i]+1)**2
    l2.append(f)
print(*l, sep='\n')
print()
print(*l2, sep='\n')