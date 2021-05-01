# объявление функции
def is_palindrome(text):
    t = txt.replace(' ', '')
    t = t.replace('-', '')
    t = t.replace('?', '')
    t = t.replace('!', '')
    t = t.replace('.', '')
    t = t.replace(',', '')
    t = t.lower()
    for _ in range(len(t)):
        if t[::-1] == t:
            return True
        else:
            return False
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))