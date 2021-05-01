text = input()
def is_pangram(text):
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    t = text.lower()
    if len(t)>=26:
        for i in range(len(t)):
            if t[i] in al:
                al.remove(t[i])
        if len(al)==0:
            return True
        else:
            return False
    return False
print(is_pangram(text))