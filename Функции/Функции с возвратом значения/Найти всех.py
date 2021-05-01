def find_all(s, symbol):
    s = [i for i in s]
    target = []
    for i in range(len(s)):
        if s[i] == symbol:
            target.append(i)
    return target

s = input()
symbol = input()
print(find_all(s, symbol))