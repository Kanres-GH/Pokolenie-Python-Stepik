a = int(input())
b = int(input())
max = 0
smax = 0
for i in range(a, b + 1):
    sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum += j
    if sum >= smax:
        smax = sum
        max = i
print(max, smax)