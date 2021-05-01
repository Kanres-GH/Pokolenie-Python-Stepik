from math import log
total = 0
n = int(input())
for i in range(n):
    total+=1/(i+1)
print(total-log(n))