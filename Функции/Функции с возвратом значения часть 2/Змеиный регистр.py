txt = input()
def convert_to_python_case(text):
    t1 = txt
    t2 = txt.lower()
    t3 = [t2[0]]
    for i in range(1,len(t1)):
        if t1[i] == t2[i]:
            t3.append(t2[i])
        else:
            t3.append('_')
            t3.append(t2[i])
    return t3

print(*convert_to_python_case(txt),sep='')