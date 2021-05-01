n = int(input())
flag = False
max_digit = -100
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        flag = True
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if flag == True:
    print(max_digit)
else:
    print('NO')