"""
Простыe тесты для проверки работы программ лабораторной работы 9.
Эти тесты проверяют основные функции без использования unittest.
"""

import sys
import os

# Добавляем путь к модулям
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import lab_9_1
import lab_9_2
import lab_9_3
import lab_9_4
import lab_9_5
import lab_9_6
import lab_9_7


def test_lab_9_1():
    """Тест программы 1 - Создание матрицы M из массивов A и B"""
    print("Тестирование программы 1...")
    
    # Тест функции проверки полного квадрата
    assert lab_9_1.is_perfect_square(0) == True
    assert lab_9_1.is_perfect_square(1) == True
    assert lab_9_1.is_perfect_square(4) == True
    assert lab_9_1.is_perfect_square(9) == True
    assert lab_9_1.is_perfect_square(16) == True
    assert lab_9_1.is_perfect_square(-1) == False
    assert lab_9_1.is_perfect_square(2) == False
    assert lab_9_1.is_perfect_square(3) == False
    
    # Тест подсчета полных квадратов в строке
    matrix = [[1, 4, 3, 9], [2, 5, 16, 7]]
    assert lab_9_1.count_perfect_squares_in_row(matrix, 0) == 3  # 1, 4, 9
    assert lab_9_1.count_perfect_squares_in_row(matrix, 1) == 1  # 16
    
    print("✅ Программа 1: Все тесты прошли")


def test_lab_9_2():
    """Тест программы 2 - Поворот квадратной матрицы"""
    print("Тестирование программы 2...")
    
    # Тест поворота по часовой стрелке
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    lab_9_2.rotate_clockwise(matrix)
    assert matrix == expected
    
    # Тест поворота против часовой стрелки
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    lab_9_2.rotate_counterclockwise(matrix)
    assert matrix == expected
    
    print("✅ Программа 2: Все тесты прошли")


def test_lab_9_3():
    """Тест программы 3 - Подсчет элементов матрицы A больше среднего столбцов матрицы B"""
    print("Тестирование программы 3...")
    
    # Тест вычисления средних значений столбцов
    matrix = [[1, 2], [3, 4], [5, 6]]
    expected = [3.0, 4.0]  # (1+3+5)/3, (2+4+6)/3
    result = lab_9_3.calculate_column_averages(matrix)
    assert result == expected
    
    # Тест подсчета элементов больше среднего
    matrix_a = [[1, 2], [3, 4], [5, 6]]
    averages = [3.0, 4.0]
    expected = [2, 2]  # В первом столбце 3,5 > 3.0, во втором 4,6 > 4.0
    result = lab_9_3.count_greater_than_average(matrix_a, averages)
    assert result == expected
    
    # Тест умножения столбцов на значения
    matrix = [[1, 2], [3, 4]]
    counts = [2, 0]
    expected = [[2, 2], [6, 4]]  # Первый столбец умножается на 2, второй остается
    lab_9_3.multiply_columns_by_counts(matrix, counts)
    assert matrix == expected
    
    print("✅ Программа 3: Все тесты прошли")


def test_lab_9_4():
    """Тест программы 4 - Поиск максимальных элементов в заданных строках"""
    print("Тестирование программы 4...")
    
    # Тест поиска максимальных элементов в строках
    matrix = [[1, 5, 3], [2, 8, 1], [9, 2, 4]]
    row_indices = [0, 1, 2]
    expected = [5, 8, 9]
    result = lab_9_4.find_max_in_rows(matrix, row_indices)
    assert result == expected
    
    # Тест вычисления среднего арифметического
    array = [1, 2, 3, 4, 5]
    expected = 3.0
    result = lab_9_4.calculate_average(array)
    assert result == expected
    
    # Тест с пустым массивом
    result_empty = lab_9_4.calculate_average([])
    assert result_empty == 0
    
    print("✅ Программа 4: Все тесты прошли")


def test_lab_9_5():
    """Тест программы 5 - Умножение матриц"""
    print("Тестирование программы 5...")
    
    # Тест умножения матриц
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]  # 1*5+2*7=19, 1*6+2*8=22, 3*5+4*7=43, 3*6+4*8=50
    result = lab_9_5.multiply_matrices(matrix_a, matrix_b)
    assert result == expected
    
    # Тест с матрицами разных размеров
    matrix_a2 = [[1, 2, 3]]
    matrix_b2 = [[4], [5], [6]]
    expected2 = [[32]]  # 1*4+2*5+3*6=32
    result2 = lab_9_5.multiply_matrices(matrix_a2, matrix_b2)
    assert result2 == expected2
    
    print("✅ Программа 5: Все тесты прошли")


def test_lab_9_6():
    """Тест программы 6 - Преобразование матрицы символов"""
    print("Тестирование программы 6...")
    
    # Тест проверки гласных букв
    assert lab_9_6.is_vowel('a') == True
    assert lab_9_6.is_vowel('E') == True
    assert lab_9_6.is_vowel('i') == True
    assert lab_9_6.is_vowel('O') == True
    assert lab_9_6.is_vowel('u') == True
    assert lab_9_6.is_vowel('b') == False
    assert lab_9_6.is_vowel('Z') == False
    assert lab_9_6.is_vowel('1') == False
    assert lab_9_6.is_vowel('@') == False
    
    # Тест проверки согласных букв
    assert lab_9_6.is_consonant('b') == True
    assert lab_9_6.is_consonant('C') == True
    assert lab_9_6.is_consonant('z') == True
    assert lab_9_6.is_consonant('M') == True
    assert lab_9_6.is_consonant('a') == False
    assert lab_9_6.is_consonant('E') == False
    assert lab_9_6.is_consonant('1') == False
    assert lab_9_6.is_consonant('@') == False
    
    # Тест преобразования матрицы символов
    matrix = [['a', 'B', 'c'], ['D', 'e', 'F']]
    expected = [['a', 'B', 'C'], ['D', 'e', 'F']]
    result = lab_9_6.transform_char_matrix(matrix)
    assert result == expected
    
    print("✅ Программа 6: Все тесты прошли")


def test_lab_9_7():
    """Тест программы 7 - Работа с трехмерным массивом"""
    print("Тестирование программы 7...")
    
    # Тест определения наибольшего измерения
    # X наибольшее
    dim, size = lab_9_7.find_max_dimension(5, 3, 2)
    assert dim == 0
    assert size == 5
    
    # Y наибольшее
    dim, size = lab_9_7.find_max_dimension(2, 7, 3)
    assert dim == 1
    assert size == 7
    
    # Z наибольшее
    dim, size = lab_9_7.find_max_dimension(2, 3, 8)
    assert dim == 2
    assert size == 8
    
    # Равные размеры
    dim, size = lab_9_7.find_max_dimension(3, 3, 3)
    assert dim == 0  # X выбирается первым
    
    # Тест вычисления индекса среза
    assert lab_9_7.get_slice_index(5) == 2  # 5//2 = 2
    assert lab_9_7.get_slice_index(4) == 2  # 4//2 = 2
    assert lab_9_7.get_slice_index(1) == 0  # 1//2 = 0
    
    # Тест извлечения среза
    # Создаем тестовый 3D массив 2x2x2
    array_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    
    # Срез по X (индекс 0)
    slice_x = lab_9_7.extract_slice(array_3d, 0, 0)
    expected_x = [[1, 2], [3, 4]]
    assert slice_x == expected_x
    
    # Срез по Y (индекс 0)
    slice_y = lab_9_7.extract_slice(array_3d, 1, 0)
    expected_y = [[1, 2], [5, 6]]
    assert slice_y == expected_y
    
    # Срез по Z (индекс 0)
    slice_z = lab_9_7.extract_slice(array_3d, 2, 0)
    expected_z = [[1, 3], [5, 7]]
    assert slice_z == expected_z
    
    print("✅ Программа 7: Все тесты прошли")


def run_all_tests():
    """Запуск всех тестов"""
    print("=" * 60)
    print("ЗАПУСК ТЕСТОВ ДЛЯ ЛАБОРАТОРНОЙ РАБОТЫ 9")
    print("=" * 60)
    
    try:
        test_lab_9_1()
        test_lab_9_2()
        test_lab_9_3()
        test_lab_9_4()
        test_lab_9_5()
        test_lab_9_6()
        test_lab_9_7()
        
        print("\n" + "=" * 60)
        print("🎉 ВСЕ ТЕСТЫ ПРОШЛИ УСПЕШНО!")
        print("=" * 60)
        return True
        
    except AssertionError as e:
        print(f"\n❌ ОШИБКА В ТЕСТАХ: {e}")
        return False
    except Exception as e:
        print(f"\n❌ НЕОЖИДАННАЯ ОШИБКА: {e}")
        return False


if __name__ == '__main__':
    success = run_all_tests()
    
    if success:
        print("\nДля запуска полных unit-тестов используйте:")
        print("python test_lab9.py")
    else:
        print("\nПроверьте код программ на наличие ошибок.")
