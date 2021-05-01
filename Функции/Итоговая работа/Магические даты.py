date = input().split('.')
def is_magic(date):
    for _ in range(len(date)):
        if int(date[0])*int(date[1])==int(date[2])%100:
            return True
        else:
            return False
print(is_magic(date))