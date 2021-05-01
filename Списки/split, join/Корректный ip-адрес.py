n = input().split('.')
cnt = 0
for i in range(len(n)):
    n[i] = int(n[i])
    if n[i]>255 or n[i]<0:
        cnt+=1
if cnt==0:
    print('ДА')
else:
    print('НЕТ')