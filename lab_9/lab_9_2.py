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
    # Поворачиваем матрицу
    for i in range(n//2):
        for j in range(i,n-1-i):
            save = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = save



def rotate_counterclockwise(matrix):
    """Поворот матрицы на 90 градусов против часовой стрелки"""
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            save = matrix[i][j]
            matrix[i][j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = save


def main():
    # Ввод размера матрицы
    n = input_square_size()
    
    # Ввод исходной матрицы
    matrix = input_matrix_int(n, n, "N")
    
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

if __name__ == "__main__":
    main()
