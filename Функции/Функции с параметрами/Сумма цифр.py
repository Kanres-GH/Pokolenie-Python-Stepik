def print_digit_sum(n):
    sum = 0
    while n!=0:
        last = n%10
        sum+=last
        n//=10
    print(sum)
n = int(input())
print_digit_sum(n)