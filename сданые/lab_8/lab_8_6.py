"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Выполнить транспонирование квадратной матрицы.
"""
import check

#  Ввод и проверка размеров матрицы
while True:
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

    if n == m:
        break
    else:
        print("\nОшибка: для транспонирования на месте матрица должна быть квадратной (N = M).")
        print("Пожалуйста, введите размеры заново.\n")

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

#  Основное задание
for i in range(n):
    for j in range(i + 1, n):
        # Обмен элементов matrix[i][j] и matrix[j][i]
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

#  Печать измененной матрицы
print("\nТранспонированная матрица:")
for i in range(n):
    print('-' * (n*10 + 1))
    print("| ",end="")
    for j in range(m):
        print(f"{matrix[i][j]:^7g}", end=" | ")
    print()
print('-' * (n*10 + 1))