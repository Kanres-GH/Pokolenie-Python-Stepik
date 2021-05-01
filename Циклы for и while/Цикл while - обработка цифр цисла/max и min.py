n = int(input())
min = 9
max = 0
while n!=0:
    if n%10>max:
        max = n%10
    if n%10<min:
        min = n%10
    n//=10 
print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)