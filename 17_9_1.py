# сортировка последовательности чисел
def binary_search(n, m, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if m == n[mid]:
           return mid
        elif m < n[mid]
           return binary_search(n,m,start,mid - 1)
        else:
           return binary_search(n, m, mid + 1, stop)

n = list(map(int,input('Введите числа через пробел ').split()))
# n.sort()
for i in range(1, len(n)):
    x = n[i]
    idx = i
    while idx > 0 and n[idx-1] > x:
        n[idx] = n[idx-1]
        idx -= 1
    n[idx] = x
# print(n)

m = int, input('Введите любое число ')


x = binary_search(n, m, 0, len(n))
if x == False:
    print('Число', m, 'в массиве не обнаружено')
else:
    print('Число', m, 'в массиве с индексом', x)


