m, n = int(input()), int(input())
if m%2!=0:
    for _ in range(m, n-1, -2):
        print(_)
else:
    for _ in range(m-1, n-1, -2):
        print(_)