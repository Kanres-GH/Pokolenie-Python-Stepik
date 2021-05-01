total = 0
n = int(input())
for i in range(n+1):
    total+=(-1)**(i+1)*i
print(total)