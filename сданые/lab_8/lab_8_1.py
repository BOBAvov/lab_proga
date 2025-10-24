"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Найти в матрице строку с наибольшим количеством
            подряд идущих одинаковых элементов.
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
        row_str = input(f"Строка {i+1}: ")
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

#  Основное задание
max_sequence_len = 1
row_with_max_sequence = 0

for i in range(n):
    current_max_len = 1

    current_len = 1
    for j in range(1, m):
            if check.float_equal(matrix[i][j], matrix[i][j-1]):
                current_len += 1
            else:
                current_len = 1
            if current_len > current_max_len:
                current_max_len = current_len

    if current_max_len > max_sequence_len:
        max_sequence_len = current_max_len
        row_with_max_sequence = i

#  Вывод результата
if max_sequence_len>1:
    print()
    print(f"Строка с наибольшим количеством подряд идущих одинаковых элементов: {row_with_max_sequence + 1}")
    print(f"Длина последовательности: {max_sequence_len}")
else:
    print(f"Нет подряд идущих элементов")