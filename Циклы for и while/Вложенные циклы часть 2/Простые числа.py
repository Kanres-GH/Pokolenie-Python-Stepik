a = int(input())
b = int(input())
if a>=2:
    for i in range(a, b+1):
        prime = True
        for j in range(2,i):
            if i%j==0:
                prime = False
        if prime:
            print(i)
else:
    for i in range(a+1, b+1):
        prime = True
        for j in range(2,i):
            if i%j==0:
                prime = False
        if prime:
            print(i)