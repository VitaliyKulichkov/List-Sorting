def linear(lst, search_item) ->bool:
    """
    Функция ищет искомое число линейным способом
    :param lst: - входные данные - список чисел
    :param search_item: - искомое число
    :return: True - если элемент найден, False - если не найден
    """
    low = 0
    search_result = False

    while low < len(lst) and not search_result:
        if lst[low] == search_item:
            search_result = True
        else:
            low += 1
    return search_result

lst = [12, 34, 25, 15, 23, 11, 5, 86, 67]
value = 67

result = linear(lst, value)
if result:
    print("Элемент найден")
else:
    print("Элемент не найден")



