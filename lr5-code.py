def sort_lowercase(array):
    # Проверка на количество элементов
    if len(array) > 100:
        print("Ошибка: массив не должен превышать 100 элементов.")
        return
    
    # Извлекаем строчные буквы
    lower_case_letters = [char for char in array if char.islower()]
    
    # Сортируем строчные буквы
    lower_case_letters.sort()
    
    # Создаем новый массив с отсортированными строчными буквами
    result = []
    lower_index = 0
    
    for char in array:
        if char.islower():
            result.append(lower_case_letters[lower_index])
            lower_index += 1
        else:
            result.append(char)
    
    # Проверяем, изменился ли массив
    if result == list(array):
        print("Массив не требует изменений:", array)
    else:
        print("Преобразованный массив:", result)

# Пример использования процедуры
arrays = [
    list(input('Введите элементы первого массива через пробел: ').split(' ')),
    list(input('Введите элементы второго массива через пробел: ').split(' ')),
    list(input('Введите элементы третьего массива через пробел: ').split(' ')),
    list(input('Введите элементы четвёртого массива через пробел: ').split(' ')),
    list(input('Введите элементы пятого массива через пробел: ').split(' ')),
]


for i, arr in enumerate(arrays):
    print(f"Обработка массива {i + 1}.", end=' ')
    sort_lowercase(arr)