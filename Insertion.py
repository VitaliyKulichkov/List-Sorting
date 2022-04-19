def insertion_sort(lst) -> list:
    """Функция сортирует массив методом пузырька
    :param lst: - входные данные - список чисел
    :return: отсортированный массив
    """
    for item in range(1, len(lst)):
        current_value = lst[item]
        position = item

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value

    return lst

lst = [12, 34, 25, 15, 23, 11, 5, 87, 67]

print(f'Исходный массив: {lst}')
result = insertion_sort(lst)
print(f'Отсортированный массив: {result}')
