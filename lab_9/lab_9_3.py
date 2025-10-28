"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Подсчет элементов матрицы A больше среднего столбцов матрицы B
Вариант:    9
"""

from val_input import input_matrix_size, input_matrix_int
from val_output import print_matrix, print_info


def calculate_column_averages(matrix):
    """Вычисление среднего арифметического для каждого столбца матрицы"""
    rows = len(matrix)
    cols = len(matrix[0])
    averages = []
    
    for j in range(cols):
        sum_col = 0
        for i in range(rows):
            sum_col += matrix[i][j]
        averages.append(sum_col / rows)
    
    return averages


def count_greater_than_average(matrix_a, averages):
    """Подсчет элементов каждого столбца матрицы A, больших среднего соответствующего столбца матрицы B"""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    counts = []
    
    for j in range(cols):
        count = 0
        for i in range(rows):
            if matrix_a[i][j] > averages[j]:
                count += 1
        counts.append(count)
    
    return counts


def multiply_columns_by_counts(matrix, counts):
    """Умножение элементов каждого столбца матрицы на соответствующее значение из counts"""
    rows = len(matrix)
    cols = len(matrix[0])
    
    for j in range(cols):
        if counts[j] != 0:
            for i in range(rows):
                matrix[i][j] *= counts[j]


def main():
    print_info("Программа 3: Подсчет элементов матрицы A больше среднего столбцов матрицы B")
    print_info("Преобразование матрицы B путем умножения столбцов на посчитанные значения")
    
    # Ввод размеров матриц
    print_info("Ввод размеров матрицы A:")
    rows_a, cols_a = input_matrix_size("A")
    
    print_info("Ввод размеров матрицы B:")
    rows_b, cols_b = input_matrix_size("B")
    
    # Проверка совпадения количества столбцов
    if cols_a != cols_b:
        print_info("Ошибка: количество столбцов в матрицах A и B должно совпадать.")
        return
    
    # Ввод матриц
    print_info("\nВвод матрицы A:")
    matrix_a = input_matrix_int(rows_a, cols_a, "A")
    
    print_info("\nВвод матрицы B:")
    matrix_b = input_matrix_int(rows_b, cols_b, "B")
    
    # Вывод исходных матриц
    print_matrix(matrix_a, "Исходная матрица A:")
    print_matrix(matrix_b, "Исходная матрица B:")
    
    # Вычисление средних значений столбцов матрицы B
    averages = calculate_column_averages(matrix_b)
    print_info(f"\nСредние арифметические столбцов матрицы B: {averages}")
    
    # Подсчет элементов матрицы A, больших среднего соответствующих столбцов матрицы B
    counts = count_greater_than_average(matrix_a, averages)
    print_info(f"Количество элементов столбцов матрицы A, больших среднего соответствующих столбцов матрицы B: {counts}")
    
    # Преобразование матрицы B
    multiply_columns_by_counts(matrix_b, counts)
    
    # Вывод преобразованной матрицы B
    print_matrix(matrix_b, "Преобразованная матрица B:")
    
    print_info("\nПрограмма завершена.")


if __name__ == "__main__":
    main()
