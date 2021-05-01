n = int(input())
for i in range((n+1)//2):
    for j in range(i+1):
        print('*', end='')
    print()
for i in range(n//2):
    for j in range(n//2-i):
        print('*', end='')
    print()