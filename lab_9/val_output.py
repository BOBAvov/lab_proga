"""
Модуль вывода данных для лабораторной 9.
Содержит функции форматированного вывода матриц, массивов и 3D-массивов,
а также функции цветного вывода информационных сообщений, предупреждений и ошибок.
"""

Color_in_console = {'red' : '\033[91m', 'green': '\033[92m',
                    'yellow': '\033[93m','blue':'\033[94m',
                    'magenta':'\033[95m','cyan':'\033[96m',
                    'end': '\033[0m'}

def get_color_string(s : str,cl = '') -> str:
    if cl in Color_in_console:
        return Color_in_console[cl]+s+Color_in_console['end']
    return s

def print_matrix(matrix, title):
    """Вывод матрицы в виде форматированной таблицы"""
    print_info(f"\n{title}")
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Определяем ширину колонок
    max_width = 1
    for i in range(rows):
        for j in range(cols):
            width = len(str(matrix[i][j]))
            if width > max_width:
                max_width = width
    
    # Вывод матрицы
    print("-" * (cols * (max_width + 2) + 1))
    for i in range(rows):
        row_str = "|"
        for j in range(cols):
            row_str += f"{matrix[i][j]:^{max_width}}|"
        print(row_str)
    print("-" * (cols * (max_width + 2) + 1))


def print_matrix_with_column(matrix, column, title):
    """Вывод матрицы с дополнительным столбцом"""
    print_info(f"\n{title}")
    print("-" * (len(matrix[0]) * 8 + 12))
    
    # Заголовок
    header = "|"
    for j in range(len(matrix[0])):
        header += f"{'M[' + str(j) + ']':^7}|"
    header += f"{'S':^7}|"
    print(header)
    print("-" * (len(matrix[0]) * 8 + 12))
    
    # Строки матрицы
    for i in range(len(matrix)):
        row_str = "|"
        for j in range(len(matrix[i])):
            row_str += f"{matrix[i][j]:^7}|"
        row_str += f"{column[i]:^7}|"
        print(row_str)
    print("-" * (len(matrix[0]) * 8 + 12))


def print_char_matrix(matrix, title):
    """Вывод матрицы символов в виде форматированной таблицы"""
    print_info(f"\n{title}")
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Вывод матрицы
    print("-" * (cols * 3 + 1))
    for i in range(rows):
        row_str = "|"
        for j in range(cols):
            row_str += f"{matrix[i][j]:^2}|"
        print(row_str)
    print("-" * (cols * 3 + 1))


def print_array(array, title):
    """Вывод одномерного массива"""
    print_info(f"\n{title}: {array}")


def print_3d_array(array_3d, title):
    """Вывод трехмерного массива"""
    print_info(f"\n{title}")
    x = len(array_3d)
    y = len(array_3d[0])
    z = len(array_3d[0][0])
    
    # Определяем ширину колонок
    max_width = 1
    for i in range(x):
        for j in range(y):
            for k in range(z):
                width = len(str(array_3d[i][j][k]))
                if width > max_width:
                    max_width = width
    
    for i in range(x):
        print_info(f"\nСлой {i+1}:")
        print("-" * (z * (max_width + 2) + 1))
        for j in range(y):
            row_str = "|"
            for k in range(z):
                row_str += f"{array_3d[i][j][k]:^{max_width}}|"
            print(row_str)
        print("-" * (z * (max_width + 2) + 1))


def print_slice_matrix(matrix, title, max_dim, slice_index):
    """Вывод матрицы среза"""
    print_info(f"\n{title}")
    print_info(f"Срез по измерению {['X', 'Y', 'Z'][max_dim]} с индексом {slice_index}")
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Определяем ширину колонок
    max_width = 1
    for i in range(rows):
        for j in range(cols):
            width = len(str(matrix[i][j]))
            if width > max_width:
                max_width = width
    
    # Вывод матрицы
    print("-" * (cols * (max_width + 2) + 1))
    for i in range(rows):
        row_str = "|"
        for j in range(cols):
            row_str += f"{matrix[i][j]:^{max_width}}|"
        print(row_str)
    print("-" * (cols * (max_width + 2) + 1))



def print_info(text: str):
    """Вывод информационного текста (голубой)."""
    print(get_color_string(text, 'cyan'))


def print_warn(text: str):
    """Вывод предупреждения (желтый)."""
    print(get_color_string(text, 'yellow'))


def print_error(text: str):
    """Вывод ошибки (красный)."""
    print(get_color_string(text, 'red'))
