"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Создание матрицы M из массивов A и B, подсчет полных квадратов
Вариант:    9
"""

import math
from val_input import input_size, input_array_int
from val_output import print_matrix_with_column, print_info

def is_perfect_square(num):
    """Проверка, является ли число полным квадратом"""
    if num < 0:
        return False
    num_sqrt = int(math.sqrt(num))
    return num_sqrt * num_sqrt == num


def count_perfect_squares_in_row(matrix, row):
    """Подсчет полных квадратов в строке матрицы"""
    count = 0
    for j in range(len(matrix[row])):
        if is_perfect_square(matrix[row][j]):
            count += 1
    return count


def main():
    print_info("Программа 1: Создание матрицы M из массивов A и B")
    print_info("Формула: m[i][j] = a[i] * b[j]")
    print_info("Подсчет полных квадратов в каждой строке матрицы M")
    
    # Ввод размеров массивов
    n_a = input_size("A")
    n_b = input_size("B")
    
    # Ввод массивов
    list_a = input_array_int(n_a, "A")
    list_b = input_array_int(n_b, "B")
    
    # Создание матрицы M
    matrix = []
    for i in range(n_a):
        row = []
        for j in range(n_b):
            row.append(list_a[i] * list_b[j])
        matrix.append(row)
    
    # Подсчет полных квадратов в каждой строке
    list_s = []
    for i in range(n_a):
        count = count_perfect_squares_in_row(matrix, i)
        list_s.append(count)
    
    # Вывод результата
    print_matrix_with_column(matrix, list_s, "Матрица M и массив S (количество полных квадратов в строках):")
    
    print_info(f"\nМассив A: {list_a}")
    print_info(f"Массив B: {list_b}")
    print_info(f"Массив S: {list_s}")


if __name__ == "__main__":
    main()
