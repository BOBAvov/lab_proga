# Вспомогательный модуль для проверки вводимых данных.
epsilon = 1e-12
# Проверка является ли строка числом
def is_integer_string(s: str) -> bool:
    if not s:
        return False
    start_index = 0
    if s.startswith("-"):
        if len(s) == 1:
            return False
        start_index = 1
    if start_index >= len(s):
        return False
    for i in range(start_index, len(s)):
        if s[i] not in "0123456789":
            return False
    return True

# Проверка строки на то является ли она вещественным числом
def is_float_string(s: str) -> bool:
    if not s:
        return False

    # Проверяем e в строке
    if 'e' in s.lower():
        parts = s.lower().split('e')
        if len(parts) != 2:
            return False
        
        # Проверяем мантиссу (часть до 'e')
        mantissa = parts[0]
        if not mantissa:
            return False
        
        # Проверяем экспоненту (часть после 'e')
        exponent = parts[1]
        if not exponent:
            return False
        
        # Мантисса должна быть валидным float числом
        if not is_float_string(mantissa):
            return False
        
        # Экспонента должна быть валидным целым числом
        if not is_integer_string(exponent):
            return False
        
        return True

    start_index = 0
    if s[0] in "+-":
        if len(s) == 1:
            return False
        start_index = 1

    if start_index >= len(s):
        return False

    dot_found = False
    digit_found = False

    # Проверяем оставшуюся часть строки
    for i in range(start_index, len(s)):
        char = s[i]

        if char == '.':
            if dot_found:
                return False
            dot_found = True
        elif char in "0123456789":
            digit_found = True
        else:
            return False

    # Строка должна содержать хотя бы одну цифру (чтобы отсечь случаи "." или "-.")
    if not digit_found:
        return False

    return True

# Проверяет, состоит ли строка s из n целых чисел, разделенных пробелами.
def string_is_float_list(s: str, n: int) -> bool:
    parts = s.split()
    if len(parts) != n:
        return False
    for part in parts:
        if not is_float_string(part):
            return False
    return True

# Сравнение двух float чисел с учетом epsilon
def float_equal(a: float, b: float, e: float = epsilon) -> bool:
    return abs(a - b) < e

# Проверка, что float число близко к нулю
def float_is_zero(a: float, e: float = epsilon) -> bool:
    return abs(a) < e