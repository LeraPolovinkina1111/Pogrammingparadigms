# ввод х о в матрицу
from mas import massiv
from vvod import vvod_znach
mas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = 0
z = 0


def defended_mas(mas):
    mas[x][y] = z
    print(mas)
    return " "


#print(defended_mas(mas))


# mas[mas.index(x,y)] = z


for i in range(len(mas)):
    if mas[i] == x:
        mas[i] = z

print(mas)