# создание массива с 0
import numpy as np 

mas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def massiv(mas):
    for i in mas:
        for i2 in i:
            print(i2, end=' ')

        print()
    return " "


print(massiv(mas))
