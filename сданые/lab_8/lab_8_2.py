"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Переставить местами строки с наибольшим и наименьшим
            количеством отрицательных элементов.
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

#  Основное задание: поиск и перестановка строк 

min_neg_count = m + 1
max_neg_count = -1
min_idx, max_idx = 0, 0

for i in range(n):
    current_neg_count = 0
    for j in range(m):
        if matrix[i][j] < 0:
                current_neg_count += 1

    if current_neg_count < min_neg_count:
            min_neg_count = current_neg_count
            min_idx = i

    if current_neg_count > max_neg_count:
            max_neg_count = current_neg_count
            max_idx = i
if n>1:
    if min_idx != max_idx:
            matrix[min_idx], matrix[max_idx] = matrix[max_idx], matrix[min_idx]
            print(f"\nПереставлены строки {min_idx + 1} и {max_idx + 1}.")
    else:
        print("\nСтроки для перестановки совпадают. Изменений нет.")
else:
    print("\nДля перестановки необходимо как минимум две строки.")

#  Печать измененной матрицы 
print("\nИзмененная матрица:")
for i in range(n):
    print('-' * (n*10 + 1))
    print("| ",end="")
    for j in range(m):
        print(f"{matrix[i][j]:^7g}", end=" | ")
    print()
print('-' * (n*10 + 1))