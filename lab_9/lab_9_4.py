"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Поиск максимальных элементов в заданных строках матрицы D
Вариант:    9
"""

from val_input import input_matrix_size, input_matrix_int, input_size, input_array_int
from val_output import print_matrix, print_array, print_info, print_warn,print_ans


def find_max_in_rows(matrix, row_indices):
    """Поиск максимальных элементов в заданных строках матрицы"""
    max_values = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row_idx in row_indices:
        if 0 <= row_idx < rows:
            max_val = matrix[row_idx][0]
            for j in range(1, cols):
                if matrix[row_idx][j] > max_val:
                    max_val = matrix[row_idx][j]
            max_values.append(max_val)
        else:
            print_warn(f"Предупреждение: строка {row_idx} не существует в матрице.")
            max_values.append(0)  # Значение по умолчанию для несуществующих строк
    
    return max_values


def calculate_average(array):
    """Вычисление среднего арифметического массива"""
    if len(array) == 0:
        return 0
    
    sum_val = 0
    for val in array:
        sum_val += val
    
    return sum_val / len(array)


def main():
    # Ввод размеров матрицы D
    rows_d, cols_d = input_matrix_size("D")
    
    # Ввод матрицы D
    print_info("\nВвод матрицы D:")
    matrix_d = input_matrix_int(rows_d, cols_d, "D")
    
    # Ввод размера массива I
    n_i = input_size("I")
    
    # Ввод массива I
    print_info(f"\nВвод массива I (номера строк от 0 до {rows_d-1}):")
    array_i = input_array_int(n_i, "I")
    
    # Вывод исходных данных
    print_matrix(matrix_d, "Матрица D:")
    print_ans("Массив I: ",array_i)
    
    # Поиск максимальных элементов в заданных строках
    array_r = find_max_in_rows(matrix_d, array_i)
    print_ans("Массив R (максимальные элементы)", array_r)
    
    # Вычисление среднего арифметического
    average = calculate_average(array_r)
    print_ans(f"\nСреднее арифметическое максимальных значений:", average)



if __name__ == "__main__":
    main()