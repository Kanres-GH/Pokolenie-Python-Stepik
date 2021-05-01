from math import sqrt
def solve(a, b, c):
    r1 = float()
    r2 = float()
    if b**2-4*a*c>=0:
        r1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        r2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        if r1==r2:
            return r1, r1
        else:
            return min(r1,r2), max(r1,r2)

a, b, c = int(input()), int(input()), int(input())


x1, x2 = solve(a, b, c)
print(x1, x2)