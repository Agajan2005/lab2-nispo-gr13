"""
Программа 2 (worker2).

Задача (вариант 3):
    Ищет наименьшее число из файла /var/data/data.txt
    и сохраняет его третью степень в /var/result/result.txt.
    Результат дополнительно выводится на экран.
"""

from pathlib import Path

DATA_FILE = Path("/var/data/data.txt")        # это result-1/data.txt хоста
RESULT_FILE = Path("/var/result/result.txt")  # это result/result.txt хоста


def main() -> None:
    if not DATA_FILE.exists():
        print(f"[worker2] Файл {DATA_FILE} не найден — программа 1 не отработала?")
        return

    numbers = []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                numbers.append(int(raw))
            except ValueError:
                print(f"[worker2] Пропущено нечисловое значение: {raw!r}")

    if not numbers:
        print("[worker2] В файле нет чисел — нечего обрабатывать.")
        return

    minimum = min(numbers)
    cube = minimum ** 3

    print(f"[worker2] Прочитано чисел: {len(numbers)}")
    print(f"[worker2] Минимум: {minimum}")
    print(f"[worker2] Минимум в кубе: {cube}")

    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with RESULT_FILE.open("w", encoding="utf-8") as f:
        f.write(str(cube) + "\n")

    print(f"[worker2] Результат записан в {RESULT_FILE}")


if __name__ == "__main__":
    main()