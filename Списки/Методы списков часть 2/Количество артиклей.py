s = input().split()
cnt = 0
for i in range(len(s)):
    if s[i]=='a' or s[i]=='A' or s[i]=='An' or s[i]=='an' or s[i]=='the' or s[i]=='The':
        cnt += 1
print('Общее количество артиклей:', cnt)