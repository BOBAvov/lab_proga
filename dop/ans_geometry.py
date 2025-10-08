import numpy as np


# --- Функции для ввода данных ---
def get_point(name):
    """Запрашивает у пользователя координаты точки и возвращает их как numpy array."""
    while True:
        try:
            coords = input(f"Введите координаты точки {name} (например, '1 2 3'): ")
            point = np.array([float(x) for x in coords.split()])
            if len(point) != 3:
                raise ValueError("Нужно ввести ровно 3 координаты.")
            return point
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")


def get_scalar(name):
    """Запрашивает у пользователя число и возвращает его."""
    while True:
        try:
            value = float(input(f"Введите число {name}: "))
            return value
        except ValueError:
            print("Ошибка ввода: нужно ввести число. Пожалуйста, попробуйте снова.")


# --- Основная функция для вычислений и вывода ---
def solve_geometry_problems():
    """Основная функция, которая запрашивает данные и решает все 12 задач."""
    # 1. Сбор исходных данных
    print("--- ВВОД ИСХОДНЫХ ДАННЫХ ---")
    A = get_point("A")
    B = get_point("B")
    D = get_point("D")
    A1 = get_point("A1")
    H = get_point("H")
    a = get_scalar("a")
    print("\n--- ИСХОДНЫЕ ДАННЫЕ ПРИНЯТЫ ---\n")

    # 2. Определение базовых векторов
    AB = B - A
    AD = D - A
    AA1 = A1 - A
    AH = H - A

    # --- РЕШЕНИЕ ЗАДАЧ ---

    # 1. Найти координаты точки М, делящей вектор АВ в отношении а : 1.
    print("--- ЗАДАНИЕ 1: Координаты точки M ---")
    M = (A + a * B) / (a + 1)
    print(f"Координаты точки M: {np.round(M, 4)}\n")

    # 2. Проверить, можно ли на векторах АВ и AD построить параллелограмм.
    print("--- ЗАДАНИЕ 2: Параллелограмм на AB и AD ---")
    cross_ab_ad = np.cross(AB, AD)
    if np.linalg.norm(cross_ab_ad) > 1e-9:
        print("Векторы AB и AD не коллинеарны, на них можно построить параллелограмм.")
        len_AB = np.linalg.norm(AB)
        len_AD = np.linalg.norm(AD)
        print(f"Длина стороны AB: {len_AB:.4f}")
        print(f"Длина стороны AD: {len_AD:.4f}\n")
        parallelogram_exists = True
    else:
        print("Векторы AB и AD коллинеарны, параллелограмм построить нельзя.\n")
        parallelogram_exists = False

    # 3. Найти углы между диагоналями параллелограмма ABCD.
    print("--- ЗАДАНИЕ 3: Углы между диагоналями ---")
    if parallelogram_exists:
        AC = AB + AD
        BD = AD - AB
        cos_phi = np.dot(AC, BD) / (np.linalg.norm(AC) * np.linalg.norm(BD))
        cos_phi = np.clip(cos_phi, -1.0, 1.0)
        phi_rad = np.arccos(cos_phi)
        phi_deg = np.degrees(phi_rad)
        print(f"Углы между диагоналями: {phi_deg:.4f}° и {180 - phi_deg:.4f}°\n")
    else:
        print("Параллелограмм не существует, углы найти нельзя.\n")

    # 4. Найти площадь параллелограмма ABCD.
    print("--- ЗАДАНИЕ 4: Площадь параллелограмма ---")
    if parallelogram_exists:
        area = np.linalg.norm(cross_ab_ad)
        print(f"Площадь параллелограмма ABCD: {area:.4f}\n")
    else:
        print("Параллелограмм не существует, площадь найти нельзя.\n")

    # 5. Убедиться, что на векторах АВ, AD, АА1 можно построить параллелепипед.
    print("--- ЗАДАНИЕ 5: Объем и высота параллелепипеда ---")
    mixed_prod = np.dot(cross_ab_ad, AA1)
    if abs(mixed_prod) > 1e-9 and parallelogram_exists:
        print("Векторы AB, AD, AA1 не компланарны, на них можно построить параллелепипед.")
        volume = abs(mixed_prod)
        area_base = np.linalg.norm(cross_ab_ad)
        height = volume / area_base
        print(f"Объем параллелепипеда: {volume:.4f}")
        print(f"Длина высоты, опущенной на основание ABCD: {height:.4f}\n")
        parallelepiped_exists = True
    else:
        print("Векторы компланарны, параллелепипед построить нельзя (вырожденный случай).\n")
        parallelepiped_exists = False

    # 6. Найти разложение вектора АН по векторам АВ, AD, АА1.
    print("--- ЗАДАНИЕ 6: Разложение вектора AH ---")
    if parallelepiped_exists:
        matrix = np.array([AB, AD, AA1]).T
        try:
            coeffs = np.linalg.solve(matrix, AH)
            print(f"AH = ({coeffs[0]:.4f})*AB + ({coeffs[1]:.4f})*AD + ({coeffs[2]:.4f})*AA1\n")
        except np.linalg.LinAlgError:
            print("Невозможно найти разложение, т.к. векторы линейно зависимы.\n")
    else:
        print("Разложение невозможно, так как базисные векторы компланарны.\n")

    # 7. Найти проекцию вектора АH на вектор АА1.
    print("--- ЗАДАНИЕ 7: Проекция вектора AH на AA1 ---")
    proj_ah_on_aa1 = np.dot(AH, AA1) / np.linalg.norm(AA1)
    print(f"Скалярная проекция вектора AH на вектор AA1: {proj_ah_on_aa1:.4f}\n")

    # 8. Найти уравнение плоскости Р, проходящей через точки А, B, D.
    print("--- ЗАДАНИЕ 8: Уравнение плоскости P (ABCD) ---")
    if parallelogram_exists:
        n_p = cross_ab_ad
        d_p = -np.dot(n_p, A)
        print(f"Уравнение плоскости P: ({n_p[0]:.4f})x + ({n_p[1]:.4f})y + ({n_p[2]:.4f})z + ({d_p:.4f}) = 0\n")
    else:
        print("Точки A, B, D лежат на одной прямой, плоскость не определена однозначно.\n")

    # 9. Найти уравнение плоскости Р1 (ABB1A1).
    print("--- ЗАДАНИЕ 9: Уравнение плоскости P1 (ABB1A1) ---")
    cross_ab_aa1 = np.cross(AB, AA1)
    if np.linalg.norm(cross_ab_aa1) > 1e-9:
        n_p1 = cross_ab_aa1
        d_p1 = -np.dot(n_p1, A)
        print(f"Уравнение плоскости P1: ({n_p1[0]:.4f})x + ({n_p1[1]:.4f})y + ({n_p1[2]:.4f})z + ({d_p1:.4f}) = 0\n")
    else:
        print("Точки A, B, A1 лежат на одной прямой, плоскость не определена однозначно.\n")

    # 10. Найти расстояние между прямыми AB и CC1.
    print("--- ЗАДАНИЕ 10: Расстояние между прямыми AB и CC1 ---")
    if parallelepiped_exists:
        C = A + AB + AD
        AC_vec = C - A
        dist = abs(np.dot(AC_vec, cross_ab_aa1)) / np.linalg.norm(cross_ab_aa1)
        print(f"Расстояние между скрещивающимися прямыми AB и CC1: {dist:.4f}\n")
    else:
        print("Параллелепипед вырожден, расстояние найти нельзя.\n")

    # 11. Найти точку А2, симметричную точке А1, относительно плоскости основания ABCD.
    print("--- ЗАДАНИЕ 11: Точка A2, симметричная A1 ---")
    if parallelogram_exists:
        # Плоскость ABCD задается точкой A и нормалью n_p = AB x AD
        n_p = cross_ab_ad

        # Вектор от точки на плоскости (A) до точки, которую отражаем (A1)
        vec_A_A1 = A1 - A  # Это наш вектор AA1

        # Формула для симметричной точки: A2 = A1 - 2 * vector_projection
        # vector_projection = ( (vec_A_A1 · n_p) / |n_p|² ) * n_p

        # Скалярный множитель для проекции
        dot_product = np.dot(vec_A_A1, n_p)
        print(dot_product)
        norm_sq = np.dot(n_p, n_p)  # |n_p|²
        print(norm_sq)

        scale_factor = 2 * dot_product / norm_sq

        print(scale_factor)
        # Вычисляем симметричную точку
        A2 = A1 - scale_factor * n_p

        print(f"Точка A2, симметричная A1 относительно плоскости ABCD: {np.round(A2, 4)}\n")
    else:
        print("Невозможно найти симметричную точку, т.к. плоскость ABCD не определена.\n")

    # 12. Найти острый угол между плоскостями ABCD (P) и ABВ1А1 (P1).
    print("--- ЗАДАНИЕ 12: Угол между плоскостями P и P1 ---")
    if parallelogram_exists and np.linalg.norm(cross_ab_aa1) > 1e-9:
        n_p = cross_ab_ad
        n_p1 = cross_ab_aa1
        cos_psi = abs(np.dot(n_p, n_p1)) / (np.linalg.norm(n_p) * np.linalg.norm(n_p1))
        cos_psi = np.clip(cos_psi, -1.0, 1.0)
        psi_rad = np.arccos(cos_psi)
        psi_deg = np.degrees(psi_rad)
        print(f"Острый угол между плоскостями ABCD и ABB1A1: {psi_deg:.4f}°\n")
    else:
        print("Одна из плоскостей не определена, угол найти нельзя.\n")


# --- Запуск программы ---
if __name__ == "__main__":
    solve_geometry_problems()