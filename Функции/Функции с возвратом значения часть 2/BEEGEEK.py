psw = input().split(':')
cnt = 0
def is_palindrome(psw):
    if psw[0][::-1]==psw[0]:
        return True
    else:
        return False
def is_even(psw):
    if int(psw[2])%2==0:
        return True
    else:
        return False
def is_prime(psw):
    if int(psw[1]) == 1:
        return False
    for i in range(2, int(psw[1])):
        if int(psw[1]) % i == 0:
            return False
    return True
def is_valid_password(password):
    if len(psw)==3:
        if is_palindrome(psw) ==True and is_prime(psw) == True and is_even(psw) == True:
            return True
        else:
            return False
    return False
print(is_valid_password(psw))