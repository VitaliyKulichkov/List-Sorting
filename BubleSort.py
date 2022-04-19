def buble_sort(lst) -> list:
    """Функция сортирует массив методом пузырька
    :param lst: - входные данные - список чисел
    :return: отсортированный массив
    """
    for num in range(len(lst)-1, 0, -1):
        for item in range(num):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]

    return lst

lst = [12, 34, 25, 15, 23, 11, 5, 87, 67]

print(f'Исходный массив: {lst}')
result = buble_sort(lst)
print(f'Отсортированный массив: {result}')
