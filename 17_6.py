array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
n = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента

    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
        n = n + 1
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(n)
