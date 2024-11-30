import random

# Генерация списка из m случайных положительных целых чисел
m = 10  # Количество чисел в списке
max_value = 100  # Максимальное значение для случайных чисел

# Создаем список случайных положительных целых чисел
positive_numbers = [random.randint(1, max_value) for _ in range(m)]

# Выводим список
print(positive_numbers)