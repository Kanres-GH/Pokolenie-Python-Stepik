n = input().split()
s = [i[1:] for i in n]
s2 = [i[:1] for i in n]
s3 = [s[i]+s2[i] for i in range(len(n))]
print(*s3, sep='ки ', end='ки')