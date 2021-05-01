n = int(input())
l = list()
l2 = list()
l3 = list()
cnt = 0
for _ in range(n):
    s = input()
    l.append(s)
k = int(input())
for _ in range(k):
    p = input()
    l2.append(p)
for i in l:
    for j in l2:
        if j.lower() not in i.lower():
            break
    else:
        print(i)