# быстрая сортировка

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    element = arr[0]
    left = list(filter(lambda i: i < element, arr))
    center = [i for i in arr if i == element]
    right = list(filter(lambda i: i > element, arr))
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([5, 2, 9, 0, 1, 5, 3]))
