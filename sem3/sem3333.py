# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими.

# функция создания массива
import numpy as np
mas = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def massiv(mas):
    print("-" * 13)
    for i in range(3):
        print("|", mas[0 + i * 3], "|", mas[1 + i * 3], "|", mas[2 + i * 3], "|")
        print("-" * 13)

print(massiv(mas))


# фукнция ввода данных
x = 0
z = 0


#def vvod_znach(x, z):


def vvod_znach(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(mas[player_answer - 1]) not in "XO":
                mas[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

print(massiv(mas))


def check_win(mas):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if mas[each[0]] == mas[each[1]] == mas[each[2]]:
            return mas[each[0]]
    return False

def main(mas):
    counter = 0
    win = False
    while not win:
        massiv(mas)
        if counter % 2 == 0:
            vvod_znach("X")
        else:
            vvod_znach("O")
        counter += 1

        tmp = check_win(mas)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    massiv(mas)

    
print(main(mas))

input("Нажмите Enter для выхода!")