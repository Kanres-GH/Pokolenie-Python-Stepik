flag = True
total = 1
for i in range(10):
    a = int(input())
    if a == 0:
        flag = False
    else:
        total = total * a
print(total)