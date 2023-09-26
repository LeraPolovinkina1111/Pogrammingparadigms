# 1Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_list_imperative(numbers):
      for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

             pass
        return numbers

numbers=[22,12,45,66,7,1]


# 2Написать точно такую же процедуру, но в декларативном стиле


def sort_list_declarative(numbers):





    pass
print(sort_list_imperative(numbers))