n = int(input())
l = list()
for i in range(n):
    s = input()
    st = s.lower()
    l.append(s)
p = input()
for i in range(n):
    if p.lower() in l[i].lower():
        print(l[i])