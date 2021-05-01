abc = 'abcdefghijklmnopqrstuvwxyz'
l = list()
for i in range(26):
    l.append(abc[i]*(i+1))
print(l)