"""
Тесты для лабораторной работы 9.
Содержит unit-тесты для всех программ.
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Добавляем путь к модулям
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Импортируем модули для тестирования
import lab_9_1
import lab_9_2
import lab_9_3
import lab_9_4
import lab_9_5
import lab_9_6
import lab_9_7


class TestLab91(unittest.TestCase):
    """Тесты для программы 1 - Создание матрицы M из массивов A и B"""
    
    def test_is_perfect_square(self):
        """Тест функции проверки полного квадрата"""
        self.assertTrue(lab_9_1.is_perfect_square(0))
        self.assertTrue(lab_9_1.is_perfect_square(1))
        self.assertTrue(lab_9_1.is_perfect_square(4))
        self.assertTrue(lab_9_1.is_perfect_square(9))
        self.assertTrue(lab_9_1.is_perfect_square(16))
        self.assertFalse(lab_9_1.is_perfect_square(-1))
        self.assertFalse(lab_9_1.is_perfect_square(2))
        self.assertFalse(lab_9_1.is_perfect_square(3))
        self.assertFalse(lab_9_1.is_perfect_square(5))
    
    def test_count_perfect_squares_in_row(self):
        """Тест подсчета полных квадратов в строке"""
        matrix = [[1, 4, 3, 9], [2, 5, 16, 7]]
        self.assertEqual(lab_9_1.count_perfect_squares_in_row(matrix, 0), 3)  # 1, 4, 9
        self.assertEqual(lab_9_1.count_perfect_squares_in_row(matrix, 1), 1)  # 16


class TestLab92(unittest.TestCase):
    """Тесты для программы 2 - Поворот квадратной матрицы"""
    
    def test_rotate_clockwise(self):
        """Тест поворота по часовой стрелке"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        lab_9_2.rotate_clockwise(matrix)
        self.assertEqual(matrix, expected)
    
    def test_rotate_counterclockwise(self):
        """Тест поворота против часовой стрелки"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        lab_9_2.rotate_counterclockwise(matrix)
        self.assertEqual(matrix, expected)


class TestLab93(unittest.TestCase):
    """Тесты для программы 3 - Подсчет элементов матрицы A больше среднего столбцов матрицы B"""
    
    def test_calculate_column_averages(self):
        """Тест вычисления средних значений столбцов"""
        matrix = [[1, 2], [3, 4], [5, 6]]
        expected = [3.0, 4.0]  # (1+3+5)/3, (2+4+6)/3
        result = lab_9_3.calculate_column_averages(matrix)
        self.assertEqual(result, expected)
    
    def test_count_greater_than_average(self):
        """Тест подсчета элементов больше среднего"""
        matrix_a = [[1, 2], [3, 4], [5, 6]]
        averages = [3.0, 4.0]
        expected = [2, 2]  # В первом столбце 3,5 > 3.0, во втором 4,6 > 4.0
        result = lab_9_3.count_greater_than_average(matrix_a, averages)
        self.assertEqual(result, expected)
    
    def test_multiply_columns_by_counts(self):
        """Тест умножения столбцов на значения"""
        matrix = [[1, 2], [3, 4]]
        counts = [2, 0]
        expected = [[2, 2], [6, 4]]  # Первый столбец умножается на 2, второй остается
        lab_9_3.multiply_columns_by_counts(matrix, counts)
        self.assertEqual(matrix, expected)


class TestLab94(unittest.TestCase):
    """Тесты для программы 4 - Поиск максимальных элементов в заданных строках"""
    
    def test_find_max_in_rows(self):
        """Тест поиска максимальных элементов в строках"""
        matrix = [[1, 5, 3], [2, 8, 1], [9, 2, 4]]
        row_indices = [0, 1, 2]
        expected = [5, 8, 9]
        result = lab_9_4.find_max_in_rows(matrix, row_indices)
        self.assertEqual(result, expected)
    
    def test_calculate_average(self):
        """Тест вычисления среднего арифметического"""
        array = [1, 2, 3, 4, 5]
        expected = 3.0
        result = lab_9_4.calculate_average(array)
        self.assertEqual(result, expected)
        
        # Тест с пустым массивом
        result_empty = lab_9_4.calculate_average([])
        self.assertEqual(result_empty, 0)


class TestLab95(unittest.TestCase):
    """Тесты для программы 5 - Умножение матриц"""
    
    def test_multiply_matrices(self):
        """Тест умножения матриц"""
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]  # 1*5+2*7=19, 1*6+2*8=22, 3*5+4*7=43, 3*6+4*8=50
        result = lab_9_5.multiply_matrices(matrix_a, matrix_b)
        self.assertEqual(result, expected)
        
        # Тест с матрицами разных размеров
        matrix_a2 = [[1, 2, 3]]
        matrix_b2 = [[4], [5], [6]]
        expected2 = [[32]]  # 1*4+2*5+3*6=32
        result2 = lab_9_5.multiply_matrices(matrix_a2, matrix_b2)
        self.assertEqual(result2, expected2)


class TestLab96(unittest.TestCase):
    """Тесты для программы 6 - Преобразование матрицы символов"""
    
    def test_is_vowel(self):
        """Тест проверки гласных букв"""
        self.assertTrue(lab_9_6.is_vowel('a'))
        self.assertTrue(lab_9_6.is_vowel('E'))
        self.assertTrue(lab_9_6.is_vowel('i'))
        self.assertTrue(lab_9_6.is_vowel('O'))
        self.assertTrue(lab_9_6.is_vowel('u'))
        self.assertFalse(lab_9_6.is_vowel('b'))
        self.assertFalse(lab_9_6.is_vowel('Z'))
        self.assertFalse(lab_9_6.is_vowel('1'))
        self.assertFalse(lab_9_6.is_vowel('@'))
    
    def test_is_consonant(self):
        """Тест проверки согласных букв"""
        self.assertTrue(lab_9_6.is_consonant('b'))
        self.assertTrue(lab_9_6.is_consonant('C'))
        self.assertTrue(lab_9_6.is_consonant('z'))
        self.assertTrue(lab_9_6.is_consonant('M'))
        self.assertFalse(lab_9_6.is_consonant('a'))
        self.assertFalse(lab_9_6.is_consonant('E'))
        self.assertFalse(lab_9_6.is_consonant('1'))
        self.assertFalse(lab_9_6.is_consonant('@'))
    
    def test_transform_char_matrix(self):
        """Тест преобразования матрицы символов"""
        matrix = [['a', 'B', 'c'], ['D', 'e', 'F']]
        expected = [['a', 'B', 'C'], ['D', 'e', 'F']]
        result = lab_9_6.transform_char_matrix(matrix)
        self.assertEqual(result, expected)


class TestLab97(unittest.TestCase):
    """Тесты для программы 7 - Работа с трехмерным массивом"""
    
    def test_find_max_dimension(self):
        """Тест определения наибольшего измерения"""
        # X наибольшее
        dim, size = lab_9_7.find_max_dimension(5, 3, 2)
        self.assertEqual(dim, 0)
        self.assertEqual(size, 5)
        
        # Y наибольшее
        dim, size = lab_9_7.find_max_dimension(2, 7, 3)
        self.assertEqual(dim, 1)
        self.assertEqual(size, 7)
        
        # Z наибольшее
        dim, size = lab_9_7.find_max_dimension(2, 3, 8)
        self.assertEqual(dim, 2)
        self.assertEqual(size, 8)
        
        # Равные размеры
        dim, size = lab_9_7.find_max_dimension(3, 3, 3)
        self.assertEqual(dim, 0)  # X выбирается первым
    
    def test_get_slice_index(self):
        """Тест вычисления индекса среза"""
        self.assertEqual(lab_9_7.get_slice_index(5), 2)  # 5//2 = 2
        self.assertEqual(lab_9_7.get_slice_index(4), 2)  # 4//2 = 2
        self.assertEqual(lab_9_7.get_slice_index(1), 0)  # 1//2 = 0
    
    def test_extract_slice(self):
        """Тест извлечения среза"""
        # Создаем тестовый 3D массив 2x2x2
        array_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        
        # Срез по X (индекс 0)
        slice_x = lab_9_7.extract_slice(array_3d, 0, 0)
        expected_x = [[1, 2], [3, 4]]
        self.assertEqual(slice_x, expected_x)
        
        # Срез по Y (индекс 0)
        slice_y = lab_9_7.extract_slice(array_3d, 1, 0)
        expected_y = [[1, 2], [5, 6]]
        self.assertEqual(slice_y, expected_y)
        
        # Срез по Z (индекс 0)
        slice_z = lab_9_7.extract_slice(array_3d, 2, 0)
        expected_z = [[1, 3], [5, 7]]
        self.assertEqual(slice_z, expected_z)


class TestIntegration(unittest.TestCase):
    """Интеграционные тесты"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_lab_9_1_integration(self, mock_print, mock_input):
        """Интеграционный тест программы 1"""
        # Настраиваем моки
        mock_input.side_effect = ['2', '3', '1 2', '3 4 5']
        
        # Запускаем программу
        lab_9_1.main()
        
        # Проверяем, что функция была вызвана
        self.assertTrue(mock_print.called)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_lab_9_2_integration(self, mock_print, mock_input):
        """Интеграционный тест программы 2"""
        # Настраиваем моки
        mock_input.side_effect = ['2', '1 2', '3 4']
        
        # Запускаем программу
        lab_9_2.main()
        
        # Проверяем, что функция была вызвана
        self.assertTrue(mock_print.called)


def run_tests():
    """Запуск всех тестов"""
    # Создаем тестовый набор
    test_suite = unittest.TestSuite()
    
    # Добавляем тесты
    test_classes = [
        TestLab91, TestLab92, TestLab93, TestLab94,
        TestLab95, TestLab96, TestLab97, TestIntegration
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    print("Запуск тестов для лабораторной работы 9...")
    success = run_tests()
    
    if success:
        print("\n✅ Все тесты прошли успешно!")
    else:
        print("\n❌ Некоторые тесты не прошли.")
    
    print(f"\nДля запуска отдельных тестов используйте:")
    print(f"python -m unittest test_lab9.TestLab91")
    print(f"python -m unittest test_lab9.TestLab92")
    print(f"и т.д.")
