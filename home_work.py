import random
import time

size = 1000  # Количество чисел в списке
max_value = 10000  # Максимальное значение для случайных чисел

def generate_random_list(size, max_value):
    """Генерирует список случайных положительных целых чисел."""
    return [random.randint(1, max_value) for _ in range(size)]

def measure_sort_time(sort_function, data):
    """Измеряет время выполнения функции сортировки."""
    start_time = time.time()  # Запоминаем время начала
    sort_function(data)        # Выполняем сортировку
    end_time = time.time()     # Запоминаем время окончания
    return end_time - start_time  # Возвращаем разницу во времени


# быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    element = arr[0]
    left = list(filter(lambda i: i < element, arr))
    center = [i for i in arr if i == element]
    right = list(filter(lambda i: i > element, arr))
    return quick_sort(left) + center + quick_sort(right)


# сортировка выбором
def selection_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]


# сортировка вставками
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Генерация случайного списка
random_list = generate_random_list(size, max_value)
# print(f"Список для сортировки:{random_list}")

# Копируем одинаковый список для сортировки
quick_list = random_list.copy()
selection_list = random_list.copy()
insert_list = random_list.copy()

# Измеряем время сортировки:
quick_sort_time = measure_sort_time(quick_sort, quick_list)
selection_sort_time = measure_sort_time(selection_sort, selection_list)
insert_sort_time = measure_sort_time(insert_sort, insert_list)

print (f"Количество чисел в списке для сортировки: {size}")
print (f"Максимально возможное число в списке для сортировки: {max_value}")
print(f"Время выполнения быстрой сортировки: {quick_sort_time:.6f} секунд")
print(f"Время выполнения сортировки выбором: {selection_sort_time:.6f} секунд")
print(f"Время выполнения сортировки вставками: {insert_sort_time:.6f} секунд")

# print(f"Отсортированный список: {quick_sort(quick_list)}")
