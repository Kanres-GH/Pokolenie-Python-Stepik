n = '1234567890'
s = input()
cnt = 0
for i in range(len(s)):
    if s[i] in n:
        cnt+=1
print(cnt)