n = int(input())
l1 = list()
for i in range(n):
    s = input()
    l1.append(s)
k = int(input())
for i in l1:
    if len(i)>=k:
        print(i[k-1],end="")