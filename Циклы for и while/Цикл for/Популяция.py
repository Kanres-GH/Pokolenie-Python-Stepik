m = float(input())
p = float(input())
n = int(input())
r = float(m+m*(p/100))
print('1', m)
for i in range(n-1):
    print(i+2, r)
    r = r + r*(p/100)