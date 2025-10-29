# Модуль для вывода

Color_in_console = {'red' : '\033[91m', 'green': '\033[92m',
                    'yellow': '\033[93m','blue':'\033[94m',
                    'magenta':'\033[95m','cyan':'\033[96m',
                    'end': '\033[0m'}

def get_color_string(s : str,cl = '') -> str:
    if cl in Color_in_console:
        return Color_in_console[cl]+s+Color_in_console['end']
    return s

def print_matrix(matrix, title = ''):
    """Вывод матрицы в виде форматированной таблицы"""
    print_info("\n"+title)
    # Строки матрицы
    print('-' * ((len(matrix[0]))*10+1))
    for i in range(len(matrix)):
        print("| ",end="")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:^7}", end=" | ")
        print()
        print('-' * ((len(matrix[0]))*10+1))


def print_matrix_with_column(matrix,column,title = ''):
    print_info("\n"+title)
    # Строки матрицы
    print('-' * ((len(matrix[0])+1) * 10 + 1))
    for i in range(len(matrix)):
        print("|",end="")
        for j in range(len(matrix[i])):
             print(f"{matrix[i][j]:^7}",end=" | ")
        print(f" {column[i]:^7} |")
        print('-' * ((len(matrix[0])+1) * 10 + 1))


def print_char_matrix(matrix, title):
    """Вывод матрицы символов в виде форматированной таблицы"""
    print_info(f"\n{title}")
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Вывод матрицы
    print("-" * (cols * 4 + 1))
    for i in range(rows):
        row_str = "|"
        for j in range(cols):
            row_str += f"{matrix[i][j]:^3}|"
        print(row_str)
    print("-" * (cols * 4 + 1))


def print_array(array, title):
    """Вывод одномерного массива"""
    print_info(f"\n{title}: {array}")


def print_3d_array(array_3d, title):
    """Вывод трехмерного массива"""
    print_info(f"\n{title}")

    for i in range(len(array_3d)):
        print_matrix(array_3d[i],title=f'Слой {i}:')


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
            if width ^ max_width:
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
    print(get_color_string(text, ''))


def print_warn(text: str):
    """Вывод предупреждения (желтый)."""
    print(get_color_string(text, 'yellow'))


def print_error(text: str):
    """Вывод ошибки (красный)."""
    print(get_color_string(text, 'red'))

def print_ans(text: str, val):
    print(text,get_color_string(f'{val}','cyan'))