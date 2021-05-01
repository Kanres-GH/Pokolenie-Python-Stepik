n = int(input())
s = 1
for i in range(n):
    for j in range(9):
        print(s, '+', j+1, '=', s+j+1)
    s+=1
    print()