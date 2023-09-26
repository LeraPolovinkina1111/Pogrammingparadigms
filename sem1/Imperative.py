# 1Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        max = i
        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[max]:
                max = j
                numbers[i], numbers[max] = numbers[max], numbers[i]


numbers = [22, 12, 45, 66, 4, 1]
sort_list_imperative(numbers)
print(numbers)

