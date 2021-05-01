largest = -100
prelargest = -100
n = int(input())
for i in range(n):
    a = int(input())
    if a>largest:
        prelargest = largest
        largest = a
    if a<largest:
        if a>prelargest:
            prelargest = a
print(largest)
print(prelargest)