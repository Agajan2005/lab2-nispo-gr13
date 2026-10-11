"""
RabbitMQ Tutorial 2 — Work Queues. Worker.

Читает задачи из 'task_queue', "выполняет" их (спит по числу точек)
и отправляет ack (подтверждение) после успешной обработки.

Запуск (можно несколько параллельно):
    python 02_work_queues/worker.py
"""

import pika
import sys
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

print("[*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    message = body.decode()
    print(f"[x] Received {message!r}")
    time.sleep(message.count("."))
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue="task_queue",
    on_message_callback=callback,
)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\n[!] Interrupted")
    try:
        sys.exit(0)
    except SystemExit:
        raise