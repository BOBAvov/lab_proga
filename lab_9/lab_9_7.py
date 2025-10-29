"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Работа с трехмерным массивом и вывод среза
Вариант:    9
"""

from val_input import input_dimensions_3d, input_3d_array
from val_output import print_3d_array, print_info, print_ans,print_matrix


def find_max_dimension(x, y, z):
    """Определение наибольшего измерения"""
    if x >= y and x >= z:
        return 0, x  # X - наибольшее измерение
    elif y >= z:
        return 1, y  # Y - наибольшее измерение
    else:
        return 2, z  # Z - наибольшее измерение


def get_slice_index(max_dim_size):
    """Вычисление индекса среза (середина размерности с округлением в меньшую сторону)"""
    return max_dim_size // 2


def extract_slice(array_3d, max_dim, slice_index):
    """Извлечение среза по наибольшему измерению"""
    x, y, z = len(array_3d), len(array_3d[0]), len(array_3d[0][0])
    
    if max_dim == 0:  # Срез по X
        slice_matrix = []
        for j in range(y):
            row = []
            for k in range(z):
                row.append(array_3d[slice_index][j][k])
            slice_matrix.append(row)
    elif max_dim == 1:  # Срез по Y
        slice_matrix = []
        for i in range(x):
            row = []
            for k in range(z):
                row.append(array_3d[i][slice_index][k])
            slice_matrix.append(row)
    else:  # Срез по Z
        slice_matrix = []
        for i in range(x):
            row = []
            for j in range(y):
                row.append(array_3d[i][j][slice_index])
            slice_matrix.append(row)
    
    return slice_matrix


def main():
    # Ввод размеров трехмерного массива
    x, y, z = input_dimensions_3d()
    
    print_info(f"Размеры трехмерного массива: {x} x {y} x {z}")
    
    # Ввод трехмерного массива
    array_3d = input_3d_array(x, y, z)
    
    # Вывод исходного трехмерного массива
    print_3d_array(array_3d, "Исходный трехмерный массив:")
    
    # Определение наибольшего измерения
    max_dim, max_size = find_max_dimension(x, y, z)
    names = ['X', 'Y', 'Z']
    print_info(f"\nНаибольшее измерение: {names[max_dim]} (размер: {max_size})")
    
    # Вычисление индекса среза
    slice_index = get_slice_index(max_size)
    print_ans(f"Индекс среза (середина с округлением в меньшую сторону): ",slice_index)
    
    # Извлечение и вывод среза
    slice_matrix = extract_slice(array_3d, max_dim, slice_index)
    print_matrix(slice_matrix, "Срез трехмерного массива:")


if __name__ == "__main__":
    main()