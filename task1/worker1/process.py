"""
Программа 1 (worker1).

Задача (вариант 3):
    Формирует файл /var/result/data.txt из первых строк
    всех файлов каталога /var/data.
"""

from pathlib import Path

DATA_DIR = Path("/var/data")       # примонтирован ./data хоста
RESULT_DIR = Path("/var/result")   # примонтирован ./result-1 хоста


def main() -> None:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(p for p in DATA_DIR.iterdir() if p.is_file())

    if not files:
        print("[worker1] В /var/data нет файлов — нечего обрабатывать.")
        return

    first_lines = []
    for path in files:
        with path.open("r", encoding="utf-8") as f:
            first_line = f.readline().strip()
        first_lines.append(first_line)
        print(f"[worker1] {path.name}: первая строка = {first_line!r}")

    out_file = RESULT_DIR / "data.txt"
    with out_file.open("w", encoding="utf-8") as f:
        for line in first_lines:
            f.write(line + "\n")

    print(f"[worker1] Записано {len(first_lines)} строк в {out_file}")


if __name__ == "__main__":
    main()