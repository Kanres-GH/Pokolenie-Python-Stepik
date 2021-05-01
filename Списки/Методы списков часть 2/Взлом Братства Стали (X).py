n = input()
n = n.replace('#', '')
for i in range(int(n)):
    string = input()
    if '#' in string:
        a = string.rfind('#')
        string = string[:a]
    print(string.rstrip())