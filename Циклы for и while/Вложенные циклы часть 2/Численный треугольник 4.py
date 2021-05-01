a = int(input())
for i in range(a):
    for k in range(i):
        print(k+1, sep='', end='')
    for j in range(i+1):
        print(i-j+1, end='')
    print()