# Тот же базовый образ, что и у worker1: python:3.12.1-slim.
# Оба воркера используют только стандартную библиотеку,
# поэтому зависимости через pip не нужны.
FROM python:3.12.1-slim

# Рабочая директория внутри контейнера.
WORKDIR /app

# Копируем скрипт программы 2.
COPY process.py /app/process.py

# Запуск скрипта. exec-форма, чтобы сигналы (например, SIGTERM
# при docker compose down) доходили до python напрямую.
CMD ["python", "/app/process.py"]