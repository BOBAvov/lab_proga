"""
Автор:      Гашев Владимир Дмитриевич
Группа:     ИУ7-12Б
Назначение: Программа для построения таблицы значений функций и графика
Вариант:    33
Функции:    s1 = b³ + 9.57b² - 243.7b + 773.6
            s2 = b * ln(b) - 18
            s3 = |s1 - s2|^(1/2)
"""
import math

# Определение констант
SHIRINA_GRAFIKA = 200
eps_0 = 1e-10
# Ввод данных с проверкой
while True:
    try:
        b_0 = float(input("Введите начальное значение аргумента b0: "))
        b_n = float(input("Введите конечное значение аргумента bn: "))
        if b_0 <= b_n:
            break
        print("Ошибка: начальное значение не может быть больше конечного.")
    except ValueError:
        print("Ошибка: введено не число. Попробуйте снова.")

while True:
    try:
        step = float(input("Введите шаг h: "))
        if step > 0:
            break
        print("Ошибка: шаг должен быть положительным числом.")
    except ValueError:
        print("Ошибка: введено не число. Попробуйте снова.")

# Предварительный проход для поиска min/max и доп. задания
b = b_0
s1_min_zadanie = float('inf')  # Минимум s1 для доп. задания
b_dlya_s1_min = b_0
s1_min_grafik = float('inf')  # Минимум s1 для масштаба графика
s1_max_grafik = float('-inf')  # Максимум s1 для масштаба графика

while b <= b_n + step / 2:
    s1 = b**3 + 9.57 * b**2 - 243.7 * b + 773.6

    # Поиск минимума для доп. задания
    if s1 < s1_min_zadanie:
        s1_min_zadanie = s1
        b_dlya_s1_min = b

    # Обновление min/max для графика (только для s1)
    if s1 < s1_min_grafik:
        s1_min_grafik = s1
    if s1 > s1_max_grafik:
        s1_max_grafik = s1
    b += step

# Вывод таблицы значений
print("\n" + "-" * 60)
print("|{:^10}|{:^15}|{:^15}|{:^15}|".format("b", "s1", "s2", "s3"))
print("-" * 60)

b = b_0
while b <= b_n + step / 2:
    s1 = b**3 + 9.57 * b**2 - 243.7 * b + 773.6
    # Проверка области определения для s2 и
    if abs(b) < eps_0:
        b = 0
    if b > 0:
        s2 = b * math.log(b) - 18
        s3 = math.sqrt(abs(s1 - s2))
        print("|{:^10.5g}|{:^15.5g}|{:^15.5g}|{:^15.5g}|".format(b, s1, s2, s3))
    else:
        # Если b <= 0, функции s2 и s3 не определены
        print("|{:^10.5g}|{:^15.5g}|{:^15}|{:^15}|".format(b, s1, "---", "---"))
    b += step
print("-" * 60)

# Вывод результата дополнительного задания
print("\nДополнительное задание:")
print("Минимальное значение s1: {:.5g}".format(s1_min_zadanie))
print("Значение b при минимуме: {:.5g}".format(b_dlya_s1_min))

# Построение графика функции s1
while True:
    try:
        kol_zas = int(input("\nВведите количество засечек (4-8): "))
        if 4 <= kol_zas <= 8:
            break
        print("Ошибка: число должно быть в диапазоне от 4 до 8.")
    except ValueError:
        print("Ошибка: введено не целое число.")

print(f"\nГрафик функции s1 = b^3 + 9.57b^2 - 243.7b + 773.6\n")

# Масштабная линейка
diapazon_s1 = s1_max_grafik - s1_min_grafik
print(" " * 8, end="")
if diapazon_s1 == 0:
    print(f"{s1_min_grafik:.5g}")
else:
    shag_zas = diapazon_s1 / (kol_zas - 1)
    i = 0
    while i < kol_zas:
        znachenie_zas = s1_min_grafik + i * shag_zas
        print(f"{znachenie_zas:<{SHIRINA_GRAFIKA // kol_zas}.5g}", end="")
        i += 1
    print()

# Расчет положения оси нуля
poz_nulya = -1
if diapazon_s1 > 0 and s1_min_grafik <= 0 <= s1_max_grafik:
    poz_nulya = int((0 - s1_min_grafik) / diapazon_s1 * (SHIRINA_GRAFIKA - 1))

# Основной цикл построения строк графика
b = b_0
while b <= b_n + step / 2:
    s1 = b**3 + 9.57 * b**2 - 243.7 * b + 773.6

    poz_zvezdy = 0
    if diapazon_s1 > 0:
        poz_zvezdy = int((s1 - s1_min_grafik) / diapazon_s1 * (SHIRINA_GRAFIKA - 1))

    # Формирование строки графика
    stroka_grafika = ""
    pos = 0
    while pos < SHIRINA_GRAFIKA:
        if pos == poz_zvezdy:
            stroka_grafika += "*"
        elif pos == poz_nulya:
            stroka_grafika += "|"
        else:
            stroka_grafika += " "
        pos += 1

    if abs(b)<eps_0:
        b = 0
    print(f"{b:<8.5g}{stroka_grafika}")
    b += step