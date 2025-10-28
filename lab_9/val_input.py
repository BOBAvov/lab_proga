"""
Модуль ввода и валидации данных для лабораторной 9.
Содержит функции ввода целых массивов, матриц, 3D-массивов и матриц символов.
"""

from check import is_integer_string, string_is_float_list
from val_output import print_error, print_info


def input_size(name):
    """Ввод положительного размера для массива с именем name."""
    while True:
        s = input(f"Введите размер массива {name}: ")
        if is_integer_string(s):
            size = int(s)
            if size > 0:
                return size
            print_error("Ошибка: размер должен быть положительным числом.")
        else:
            print_error("Ошибка: введено не целое число.")


def input_positive_int(prompt):
    """Ввод единственного положительного целого с произвольной подсказкой."""
    while True:
        s = input(prompt)
        if is_integer_string(s):
            value = int(s)
            if value > 0:
                return value
            print_error("Ошибка: число должно быть положительным.")
        else:
            print_error("Ошибка: введено не целое число.")


def input_array_int(n, name):
    """Ввод одномерного массива из n целых для массива name."""
    while True:
        s = input(f"Введите {n} элементов массива {name} через пробел: ")
        if string_is_float_list(s, n):
            return [int(float(x)) for x in s.split()]
        print_error("Ошибка: введены некорректные данные. Попробуйте снова.")


def input_matrix_size(name):
    """Ввод размеров матрицы name (строки и столбцы), оба положительные."""
    while True:
        rows_s = input(f"Введите количество строк матрицы {name}: ")
        cols_s = input(f"Введите количество столбцов матрицы {name}: ")
        if is_integer_string(rows_s) and is_integer_string(cols_s):
            rows = int(rows_s)
            cols = int(cols_s)
            if rows > 0 and cols > 0:
                return rows, cols
            print_error("Ошибка: размеры должны быть положительными числами.")
        else:
            print_error("Ошибка: введены не целые числа.")


def input_square_size():
    """Ввод размера квадратной матрицы (положительное целое)."""
    return input_positive_int("Введите размер квадратной матрицы: ")


def input_matrix_int(rows, cols, name):
    """Ввод матрицы rows x cols целых чисел для матрицы name."""
    matrix = []
    for i in range(rows):
        while True:
            s = input(f"Введите {cols} элементов строки {i + 1} матрицы {name} через пробел: ")
            if string_is_float_list(s, cols):
                row = [int(float(x)) for x in s.split()]
                matrix.append(row)
                break
            print_error("Ошибка: введены некорректные данные. Попробуйте снова.")
    return matrix


def input_char_matrix(rows, cols):
    """Ввод матрицы символов размером rows x cols."""
    matrix = []
    for i in range(rows):
        while True:
            s = input(f"Введите {cols} символов строки {i + 1} матрицы: ")
            if len(s) == cols:
                matrix.append(list(s))
                break
            print_error(f"Ошибка: введено {len(s)} символов, требуется {cols}.")
    return matrix


def input_dimensions_3d():
    """Ввод размеров трехмерного массива X, Y, Z (все положительные)."""
    x = input_positive_int("Введите размер X трехмерного массива: ")
    y = input_positive_int("Введите размер Y трехмерного массива: ")
    z = input_positive_int("Введите размер Z трехмерного массива: ")
    return x, y, z


def input_3d_array(x, y, z):
    """Ввод трехмерного массива целых чисел размера X x Y x Z."""
    array_3d = []
    for i in range(x):
        print_info(f"\nВвод слоя {i + 1} (матрица {y}x{z}):")
        layer = []
        for j in range(y):
            while True:
                s = input(f"Введите {z} элементов строки {j + 1} слоя {i + 1} через пробел: ")
                if string_is_float_list(s, z):
                    row = [int(float(val)) for val in s.split()]
                    layer.append(row)
                    break
                print_error("Ошибка: введены некорректные данные. Попробуйте снова.")
        array_3d.append(layer)
    return array_3d


