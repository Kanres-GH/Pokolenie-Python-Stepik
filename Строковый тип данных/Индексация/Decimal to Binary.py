n = int(input())
t = str()
while n!=0:
    last = n%2
    t+=str(last)
    n//=2
for i in range(len(t)-1, -1, -1):
    print(t[i], end='')