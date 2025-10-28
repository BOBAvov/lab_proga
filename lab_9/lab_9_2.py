"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Поворот квадратной матрицы на 90° по часовой и против часовой стрелки
Вариант:    9
"""

from copy import deepcopy
from val_input import input_square_size, input_matrix_int
from val_output import print_matrix, print_info


def rotate_clockwise(matrix):
    """Поворот матрицы на 90 градусов по часовой стрелке"""
    n = len(matrix)
    # Поворачиваем матрицу на месте
    # Сначала транспонируем
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Затем отражаем по горизонтали
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]


def rotate_counterclockwise(matrix):
    """Поворот матрицы на 90 градусов против часовой стрелки"""
    n = len(matrix)
    # Поворачиваем матрицу на месте
    # Сначала транспонируем
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Затем отражаем по вертикали
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]


def main():
    print_info("Программа 2: Поворот квадратной матрицы")
    print_info("Поворот на 90° по часовой стрелке, затем на 90° против часовой стрелки")
    
    # Ввод размера матрицы
    n = input_square_size()
    
    # Ввод исходной матрицы
    matrix = input_matrix_int(n, n, "")
    
    # Создаем копии для промежуточных состояний
    matrix_copy1 = deepcopy(matrix)  # Копия для первого поворота
    matrix_copy2 = deepcopy(matrix)  # Копия для второго поворота
    
    # Вывод исходной матрицы
    print_matrix(matrix, "Исходная матрица:")
    
    # Поворот на 90° по часовой стрелке
    rotate_clockwise(matrix_copy1)
    print_matrix(matrix_copy1, "После поворота на 90° по часовой стрелке:")
    
    # Поворот на 90° против часовой стрелки (из промежуточного состояния)
    rotate_counterclockwise(matrix_copy2)
    print_matrix(matrix_copy2, "После поворота на 90° против часовой стрелки:")
    
    print_info("\nПрограмма завершена.")


if __name__ == "__main__":
    main()
