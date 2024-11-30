# пузырьковая сортировка

mas = [61, 55, 63, 8, 5, 7, 4, 3, 84, 2, 1, 19, 33, 9, 11, 43]
n = len (mas)
print(n)

for run in range(n-1):
    for i in range(n-1-run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)
