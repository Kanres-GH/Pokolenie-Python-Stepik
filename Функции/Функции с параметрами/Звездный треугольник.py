def draw_triangle(fill, n):
    for i in range((n+1)//2):
        for j in range(i+1):
            print(fill, end='')
        print()
    for i in range(n//2):
        for j in range(n//2-i):
            print(fill, end='')
        print()
fill = input()
n = int(input())
draw_triangle(fill, n)