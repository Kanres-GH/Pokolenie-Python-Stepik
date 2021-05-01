def is_password_good(password):
    cnt = 0
    num = '0123456789'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(txt)>=8:
        cnt += 1
    for i in txt:
        if i in num:
            cnt+=1
            break
    for i in txt:
        if i in lower:
            cnt+=1
            break
    for i in txt:
        if i in upper:
            cnt+=1
            break
    return cnt == 4

txt = input()
print(is_password_good(txt))