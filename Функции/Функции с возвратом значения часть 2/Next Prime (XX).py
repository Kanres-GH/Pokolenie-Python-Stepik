# объявление функции
def is_prime(n):
    cnt = 0
    for i in range(1, n+1):
        if n%i==0:
            cnt += 1
    if cnt > 2 or cnt==1:
        return False
    else:
        return True
def get_next_prime(n):
    while is_prime(n) == False:
        n +=1
    return n

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n+1))