def sort_list_declarative(numbers):
    return sorted(numbers, key=lambda x: -x);


print(sort_list_declarative([1, 3, 2, 6, 5]))