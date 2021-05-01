def get_days(num):
    year = [31,28,31,30,31,30,31,31,30,31,30,31]
    return year[num-1]


num = int(input())


print(get_days(num))