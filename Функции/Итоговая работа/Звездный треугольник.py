# объявление функции
def draw_triangle():
    for i in range(8):
        print(' '*(8-i-1)+'*'*(1+i*2))

# основная программа
draw_triangle()  # вызов функции