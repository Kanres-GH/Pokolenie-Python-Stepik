s = input()
cnt = 0
for i in range(len(s)):
    if s[i]=='f':
        cnt+=1
if cnt>=2:
    print(s.find('f'), s.rfind('f'))
if cnt==1:
    print(s.find('f'))
if cnt == 0:
    print('NO')