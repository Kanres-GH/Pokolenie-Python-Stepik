n = int(input())
s = n
count = 0
while n!=0:
    last = n % 10
    count+=1
    n//=10
print((s//(10**(count-3)))%10)