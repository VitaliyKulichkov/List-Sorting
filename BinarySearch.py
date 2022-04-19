def binary_search(lst, search_item) -> bool:
    """
    Функция ищет искомое число бинарным способом
    :param lst: - входные данные - список чисел
    :param search_item: - искомое число
    :return: True - если элемент найден, False - если не найден
    """
    low = 0
    high = len(lst) - 1
    search_result = False

    while low <=high and not search_result:
        midlle = (low + high)//2
        guess = lst[midlle]
        if guess == search_item:
            search_result = True
            return search_result
        if guess > search_item:
            high = midlle - 1
        else:
            low = midlle + 1
    return search_result

lst = [12, 34, 25, 15, 23, 11, 5, 87, 67]
value = 67

result = binary_search(sorted(lst), value)
if result:
    print("Элемент найден")
else:
    print("Элемент не найден")