n = input().split()            #   n = 3 4 5 2 1
for i in range(len(n)):
    n[i] = int(n[i])
l = list(n)
i_max = n.index(max(l))
i_min = n.index(min(l))
del n[i_max]
n.insert(i_max, min(l))
del n[i_min]
n.insert(i_min, max(l))
print(*n)