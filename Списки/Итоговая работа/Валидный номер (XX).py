n = input()
s = n.replace('-','')
if s.isdigit() == False:
    print('NO')
else:
    t = n.split('-')
    l = []
    for i in range(len(t)):
        l.append(len(t[i]))
    if (l == [1, 3, 3, 4] and t[0]=='7') or (l == [3, 3, 4]):
        print('YES')
    else:
        print('NO')