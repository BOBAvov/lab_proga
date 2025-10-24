"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Найти в матрице столбец с наибольшим количеством
            нулевых элементов.
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
for i in range(n):
    print('-' * (n*10 + 1))
    print("| ",end="")
    for j in range(m):
        print(f"{matrix[i][j]:^7g}", end=" | ")
    print()
print('-' * (n*10 + 1))

#  Основное задание: поиск столбца 
max_zeros_count = -1
col_with_max_zeros = -1

for j in range(m):
    current_zeros_count = 0
    for i in range(n):
        if check.float_is_zero(matrix[i][j]):
            current_zeros_count += 1

    if current_zeros_count > max_zeros_count:
        max_zeros_count = current_zeros_count
        col_with_max_zeros = j

#  Вывод результата 
print("\nРезультат:")
if max_zeros_count > 0:
    print(f"Столбец с наибольшим количеством нулевых элементов: {col_with_max_zeros + 1}")
    print(f"Количество нулей в нем: {max_zeros_count}")
else:
    print("Нулевых элементов в матрице не найдено.")