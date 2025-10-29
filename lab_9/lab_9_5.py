"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Умножение матриц A и B
Вариант:    9
"""
from lab_9.val_output import print_warn
from val_input import input_matrix_size, input_matrix_int
from val_output import print_matrix, print_info


def multiply_matrices(matrix_a, matrix_b):
    """Умножение матриц A и B"""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    # Создаем результирующую матрицу
    matrix_c = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            sum_val = 0
            for k in range(cols_a):
                sum_val += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum_val)
        matrix_c.append(row)
    
    return matrix_c


def main():
    
    # Ввод размеров матрицы A
    print_info("Ввод размеров матрицы A:")
    rows_a, cols_a = input_matrix_size("A")
    
    # Ввод размеров матрицы B
    print_info("Ввод размеров матрицы B:")
    rows_b, cols_b = input_matrix_size("B")
    
    # Проверка возможности умножения матриц
    if cols_a != rows_b:
        print_warn("Ошибка: количество столбцов матрицы A должно равняться количеству строк матрицы B.")
        print_info(f"Матрица A: {rows_a} x {cols_a}")
        print_info(f"Матрица B: {rows_b} x {cols_b}")
        return
    
    # Ввод матриц
    matrix_a = input_matrix_int(rows_a, cols_a, "A")

    matrix_b = input_matrix_int(rows_b, cols_b, "B")
    
    # Вывод исходных матриц
    print_matrix(matrix_a, "Матрица A:")
    print_matrix(matrix_b, "Матрица B:")
    
    # Умножение матриц
    matrix_c = multiply_matrices(matrix_a, matrix_b)
    
    # Вывод результирующей матрицы
    print_matrix(matrix_c, "Матрица C:")


if __name__ == "__main__":
    main()
