n = int (input())
while n > 9:
    i = int (n%10)
    n = n//10
    n = n + i
print(n)