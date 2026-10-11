"""
RabbitMQ Tutorial 2 — Work Queues. Отправка задач.

Каждый аргумент командной строки — задача. Точки в строке
эмулируют время обработки (1 точка = 1 секунда).

Запуск:
    python 02_work_queues/new_task.py "Первая задача."
    python 02_work_queues/new_task.py "Вторая задача.."
    python 02_work_queues/new_task.py "Третья задача..."
"""

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)
channel = connection.channel()

# durable=True — очередь переживёт перезапуск брокера.
channel.queue_declare(queue="task_queue", durable=True)

message = " ".join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
    ),
)
print(f"[x] Sent {message!r}")

connection.close()