"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Переставить местами столбцы с максимальной и минимальной
            суммой элементов.
"""
import check

#  Ввод и проверка размеров матрицы 
while True:
    n_str = input("Введите количество строк (N > 0): ")
    if check.is_integer_string(n_str):
        n = int(n_str)
        if n > 0:
            break
    print("Ошибка: количество строк должно быть положительным целым числом.")

while True:
    m_str = input("Введите количество столбцов (M > 0): ")
    if check.is_integer_string(m_str):
        m = int(m_str)
        if m > 0:
            break
    print("Ошибка: количество столбцов должно быть положительным целым числом.")

#  Ввод матрицы с проверкой каждой строки 
matrix = []
print(f"Введите матрицу {n}x{m} построчно, разделяя элементы пробелами:")
for i in range(n):
    while True:
        row_str = input(f"Строка {i + 1}: ")
        if check.string_is_float_list(row_str, m):
            matrix.append([float(x) if not check.float_is_zero(float(x)) else 0 for x in row_str.split()])
            break
        print(f"Ошибка: строка должна содержать {m} чисел. Попробуйте снова.")

#  Печать исходной матрицы 
print("\nИсходная матрица:")
for i in range(n):
    print('-' * (n*10 + 1))
    print("| ",end="")
    for j in range(m):
        print(f"{matrix[i][j]:^7g}", end=" | ")
    print()
print('-' * (n*10 + 1))
#  Основное задание: поиск и перестановка столбцов
column_sums = [0] * m
for j in range(m):
    for i in range(n):
        column_sums[j] += matrix[i][j]

min_sum = column_sums[0]
max_sum = column_sums[0]
min_idx, max_idx = 0, 0

for j in range(1, m):
    if column_sums[j] < min_sum:
        min_sum = column_sums[j]
        min_idx = j
    if column_sums[j] > max_sum:
        max_sum = column_sums[j]
        max_idx = j

if min_idx != max_idx:
    for i in range(n):
        matrix[i][min_idx], matrix[i][max_idx] = matrix[i][max_idx], matrix[i][min_idx]
    print(f"\nПереставлены столбцы {min_idx + 1} (сумма {min_sum}) и {max_idx + 1} (сумма {max_sum}).")
else:
    print("\nСтолбцы для перестановки совпадают. Изменений нет.")

if n<=1:
    print("\nДля перестановки необходимо как минимум два столбца.")

#  Печать измененной матрицы 
print("\nИзмененная матрица:")
for i in range(n):
    print('-' * (n*10 + 1))
    print("| ",end="")
    for j in range(m):
        print(f"{matrix[i][j]:^7g}", end=" | ")
    print()
print('-' * (n*10 + 1))