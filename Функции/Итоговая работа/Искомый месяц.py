lan = input()
n = int(input())
def get_month(language, number):
    en = ['','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    if lan == 'ru':
        for i in range(len(ru)):
            if n == i:
                return ru[i]
    if lan == 'en':
        for i in range(len(en)):
            if n == i:
                return en[i]
print(get_month(lan, n))