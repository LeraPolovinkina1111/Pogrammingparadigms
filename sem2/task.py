# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

a = int(input("Введите любое число от 1 до 9: "))
n = int(input("Введите любое число от 1 до 9: "))

i = 1
while i <= n:
    k = i*n
    print(a,"*",i,"=",k )
    i += 1



#императивное программирование структурная реализация 