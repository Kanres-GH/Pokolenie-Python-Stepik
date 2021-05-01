cnt = 0
s = input()
max = 0
for i in s:
    cnt = s.count(i)
    if cnt>=max:
        kakoito_symbol=i
        max = cnt
print(kakoito_symbol)