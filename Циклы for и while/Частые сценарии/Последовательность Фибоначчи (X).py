f1 = f2 = 1
n = int(input())
if n==1:
    print(f1, end=' ')
elif n==2:
    print(f2, end=' ')
    print(f2, end=' ')
elif n>2:
    print(f2, end=' ')
    print(f2, end=' ')
    for i in range(1, n-1):
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')