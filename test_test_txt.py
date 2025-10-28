"""
Автотесты, сгенерированные из test.txt (лабораторная №8).
Тесты парсят описания кейсов в test.txt и запускают соответствующие скрипты lab_8_X.py,
передавая входные данные через stdin. Затем проверяют, что ожидаемая строка
встречается в выводе программы. Если целевой файл отсутствует, тест помечается как пропущенный.
"""

import io
import os
import re
import sys
import unittest
import subprocess
from pathlib import Path


ROOT = Path(__file__).parent
TEST_SPEC = ROOT / "test.txt"


class SpecTestCase:
    def __init__(self, lab_name: str, idx: int, input_text: str, expected_text: str):
        self.lab_name = lab_name  # e.g. lab_8_1.py
        self.idx = idx            # sequential test index per lab
        self.input_text = input_text.strip("\n")
        self.expected_text = expected_text.strip()


def parse_spec_file(spec_path: Path) -> list[SpecTestCase]:
    text = spec_path.read_text(encoding="utf-8")
    cases: list[SpecTestCase] = []

    # Разбиваем по разделам lab_8_X.py
    lab_sections = re.split(r"^##\s+(lab_8_\d+\.py)\b.*$", text, flags=re.M)
    # Формат: [pre, lab_name1, lab_body1, lab_name2, lab_body2, ...]
    if len(lab_sections) < 3:
        return cases

    for i in range(1, len(lab_sections), 2):
        lab_name = lab_sections[i]
        lab_body = lab_sections[i + 1]

        # Ищем блоки ```input``` + строку "Ожидаемый результат: ..."
        # В файле входные данные просто внутри тройных кавычек ```
        code_blocks = re.split(r"```", lab_body)
        # После каждого блока ожидание где-то рядом, ищем ближайшую строку Ожидаемый результат
        block_indices = [idx for idx in range(1, len(code_blocks), 2)]

        test_idx = 1
        pos = 0
        for bi in block_indices:
            input_block = code_blocks[bi]
            # Найдём после текущего блока ближайшее "Ожидаемый результат: ..." в хвосте lab_body[pos:]
            tail = lab_body[pos:]
            m = re.search(r"Ожидаемый результат:\s*(.+)", tail)
            if m:
                expected = m.group(1).strip()
                cases.append(SpecTestCase(lab_name, test_idx, input_block, expected))
                test_idx += 1
                # Сдвигаем pos после найденного ожидания, чтобы следующее соответствовало следующему блоку
                pos += m.end()
            else:
                # Нет явного ожидания — пропускаем
                pass

    return cases


def run_script_with_input(script_path: Path, input_text: str, timeout_sec: float = 2.5) -> str:
    """Запускает скрипт python с подачей input_text на stdin. Возвращает stdout."""
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout_sec,
    )
    return proc.stdout.decode("utf-8", errors="replace")


class TestLab8FromSpec(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not TEST_SPEC.exists():
            raise unittest.SkipTest("Файл test.txt не найден — нечего проверять")
        cls.cases = parse_spec_file(TEST_SPEC)
        if not cls.cases:
            raise unittest.SkipTest("Не удалось распарсить тесты из test.txt")

    def test_spec_cases(self):
        for case in self.cases:
            with self.subTest(lab=case.lab_name, idx=case.idx):
                script = ROOT / case.lab_name
                if not script.exists():
                    self.skipTest(f"{case.lab_name} отсутствует в проекте")

                # Подготовим вход: строки в блоках — по одной на input()
                input_text = case.input_text.strip("\n") + "\n"

                output = run_script_with_input(script, input_text)

                # Проверяем, что ожидаемая строка встречается в выводе
                self.assertIn(case.expected_text, output,
                              msg=f"Ожидали увидеть: '{case.expected_text}'\nВывод программы:\n{output}")


if __name__ == "__main__":
    unittest.main(verbosity=2)


