"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Программа 6 - Преобразование матрицы символов
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
    
    # Создаем копию матрицы для преобразования
    transformed_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            char = matrix[i][j]
            
            if is_consonant(char):
                # Согласные латинские буквы -> заглавные
                row.append(char.upper())
            elif is_vowel(char):
                # Гласные латинские буквы -> строчные
                row.append(char.lower())
            else:
                # Остальные символы остаются без изменений
                row.append(char)
        
        transformed_matrix.append(row)
    
    return transformed_matrix


def main():
    print_info("Программа 6: Преобразование матрицы символов")
    print_info("Согласные латинские буквы -> заглавные")
    print_info("Гласные латинские буквы -> строчные")
    
    # Ввод размеров матрицы
    rows, cols = input_matrix_size("символов")
    
    # Ввод матрицы символов
    print_info(f"\nВвод матрицы символов размером {rows}x{cols}:")
    matrix = input_char_matrix(rows, cols)
    
    # Вывод исходной матрицы
    print_char_matrix(matrix, "Исходная матрица символов:")
    
    # Преобразование матрицы
    transformed_matrix = transform_char_matrix(matrix)
    
    # Вывод преобразованной матрицы
    print_char_matrix(transformed_matrix, "Преобразованная матрица символов:")
    
    # Подсчет изменений
    consonant_count = 0
    vowel_count = 0
    unchanged_count = 0
    
    for i in range(rows):
        for j in range(cols):
            original = matrix[i][j]
            transformed = transformed_matrix[i][j]
            
            if original != transformed:
                if is_consonant(original):
                    consonant_count += 1
                elif is_vowel(original):
                    vowel_count += 1
            else:
                unchanged_count += 1
    
    print_info(f"\nСтатистика преобразования:")
    print_info(f"Согласных букв преобразовано: {consonant_count}")
    print_info(f"Гласных букв преобразовано: {vowel_count}")
    print_info(f"Символов без изменений: {unchanged_count}")
    
    print_info("\nПрограмма завершена.")


if __name__ == "__main__":
    main()
