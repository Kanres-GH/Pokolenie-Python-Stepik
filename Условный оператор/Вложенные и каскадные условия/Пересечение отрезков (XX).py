a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1==a2 and b1==b2:
    print(a1, b1)
elif a1<=a2 and b1>=b2:
    print(a2, b2)
elif a1>=a2 and b1<=b2:
    print(a1, b1)
elif a1<=a2<=b1 and b1<=b2>=a2:
    if b1==a2:
        print(b1)
    else:
        print(a2, b1)
elif a1>=a2<=b2 and b1>=b2>=a1:
    if b2==a1:
        print(b2)
    else:
        print(a1, b2)
else:
    print('пустое множество')