txt = input()
def is_correct_bracket(text):
    cnt = 0
    for i in range(len(txt)):
        if txt[0] == ')' or txt[-1] == '(':
            return False
        if txt[i] == '(':
            cnt+=1
        if txt[i] == ')':
            if cnt == 0:
                return False
            cnt-=1
    if cnt==0:
        return True
    else:
        return False

print(is_correct_bracket(txt))