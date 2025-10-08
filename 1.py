import os
import random
import time
import sys

# --- Настройки камина ---
WIDTH = 80  # Ширина камина (в символах)
HEIGHT = 25  # Высота пламени
FRAME_DELAY = 0.08  # Задержка между кадрами (в секундах)
SPARK_DENSITY = 0.05  # Плотность появления новых искр внизу

# --- ANSI escape-коды для цветов ---
# (Работают в большинстве современных терминалов Linux, macOS и Windows)
COLOR_BLACK = "\033[30m"
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_WHITE = "\033[97m"
COLOR_ORANGE = "\033[38;5;208m"  # Специальный код для оранжевого
COLOR_BROWN = "\033[38;5;94m"  # Специальный код для коричневого
COLOR_RESET = "\033[0m"


def clear_screen():
    """Очищает экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_fire_buffer(width, height):
    """Создает пустой буфер для хранения 'температуры' огня."""
    return [[0] * width for _ in range(height)]


def update_fire(buffer):
    """
    Обновляет состояние огня для следующего кадра.
    Пламя движется снизу вверх и постепенно остывает.
    """
    height = len(buffer)
    width = len(buffer[0])

    # Проходим по буферу снизу вверх
    for y in range(height - 1, -1, -1):
        for x in range(width):
            # В самом низу случайным образом создаем новые горячие искры
            if y == height - 1:
                if random.random() < SPARK_DENSITY:
                    buffer[y][x] = random.randint(80, 100)
                else:
                    buffer[y][x] = 0  # Пустое место
            else:
                # Распространяем огонь от ячеек ниже с небольшим смещением (ветер)
                # и затуханием (остывание)
                decay = random.randint(1, 3)
                wind = random.randint(-1, 1)

                source_x = x + wind
                # Проверяем, чтобы не выйти за границы
                if 0 <= source_x < width:
                    # Новая температура - это температура ячейки снизу минус затухание
                    new_heat = buffer[y + 1][source_x] - decay
                    buffer[y][x] = max(0, new_heat)  # Температура не может быть < 0


def draw_frame(buffer):
    """
    Рисует один кадр анимации, преобразуя температуру в символы и цвета.
    """
    output_lines = []

    # Рисуем пламя
    for y, row in enumerate(buffer):
        line = ""
        for x, heat in enumerate(row):
            # Выбор символа и цвета в зависимости от "температуры"
            if heat > 85:
                char = random.choice(["W", "#", "@"])
                color = COLOR_WHITE
            elif heat > 70:
                char = random.choice(["#", "*", "W"])
                color = COLOR_YELLOW
            elif heat > 50:
                char = random.choice(["*", "^", "w"])
                color = COLOR_ORANGE
            elif heat > 25:
                char = random.choice([".", "'", "`"])
                color = COLOR_RED
            else:
                char = " "
                color = ""

            # Добавляем символ с цветом в строку
            if char != " ":
                line += color + char + COLOR_RESET
            else:
                line += char
        output_lines.append(line)

    # Рисуем поленья под огнем
    log_char = "═"
    logs = [
        " " * 25 + COLOR_BROWN + log_char * 30 + COLOR_RESET,
        " " * 28 + COLOR_BROWN + log_char * 24 + COLOR_RESET,
    ]
    output_lines.extend(logs)

    # Собираем все строки в один блок и выводим на экран
    # Использование sys.stdout.write и flush() делает анимацию более плавной
    sys.stdout.write("\n".join(output_lines))
    sys.stdout.flush()


def main():
    """Основной цикл программы."""
    clear_screen()
    fire_buffer = create_fire_buffer(WIDTH, HEIGHT)
    print("Запуск консольного камина... Нажмите Ctrl+C для выхода.")
    time.sleep(2)

    try:
        while True:
            # 1. Поместить курсор в левый верхний угол (вместо полной очистки)
            sys.stdout.write("\033[H")

            # 2. Обновить состояние огня
            update_fire(fire_buffer)

            # 3. Нарисовать кадр
            draw_frame(fire_buffer)

            # 4. Подождать перед следующим кадром
            time.sleep(FRAME_DELAY)

    except KeyboardInterrupt:
        # Корректное завершение по Ctrl+C
        clear_screen()
        print(f"{COLOR_RESET}Камин погас. Хорошего дня!")


if __name__ == "__main__":
    main()