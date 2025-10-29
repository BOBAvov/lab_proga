"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Преобразование матрицы символов
Вариант:    9
"""

from val_input import input_matrix_size, input_char_matrix
from val_output import print_char_matrix, print_info


def is_vowel(char):
    """Проверка, является ли символ гласной латинской буквой"""
    vowels = "aeiouAEIOU"
    return char in vowels


def is_consonant(char):
    """Проверка, является ли символ согласной латинской буквой"""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return char in consonants


def transform_char_matrix(matrix):
    """Преобразование матрицы символов: согласные -> заглавные, гласные -> строчные"""
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        row = []
        for j in range(cols):
            if is_consonant(matrix[i][j]):
                # Согласные латинские буквы -> заглавные
                matrix[i][j] = matrix[i][j].upper()
            elif is_vowel(matrix[i][j]):
                # Гласные латинские буквы -> строчные
                matrix[i][j] = matrix[i][j].lower()



def main():
    # Ввод размеров матрицы
    rows, cols = input_matrix_size("символов")
    
    # Ввод матрицы символов
    print_info(f"\nВвод матрицы символов размером {rows}x{cols}:")
    matrix = input_char_matrix(rows, cols)
    
    # Вывод исходной матрицы
    print_char_matrix(matrix, "Исходная матрица символов:")
    
    # Преобразование матрицы
    transform_char_matrix(matrix)
    
    # Вывод преобразованной матрицы
    print_char_matrix(matrix, "Преобразованная матрица символов:")


if __name__ == "__main__":
    main()