l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [l1[i]+l2[i] for i in range(len(l1))]
print(*l3)
   