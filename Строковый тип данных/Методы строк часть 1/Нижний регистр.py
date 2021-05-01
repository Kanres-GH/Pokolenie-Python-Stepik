s = input()
n = '1234567890'
cnt = 0
for i in range(len(s)):
    if s[i]==s.lower()[i] and s[i] not in n:
        cnt+=1
print(cnt)