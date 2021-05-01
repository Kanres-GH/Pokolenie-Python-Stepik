a = int(input())
total = 0
for i in range(a):
    for j in range(i+1):
        total+=1
        print(total, end=' ')
    print()