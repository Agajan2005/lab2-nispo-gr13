"""
RabbitMQ Tutorial 3 — Publish/Subscribe. Подписчик.

Создаёт временную очередь, привязывает её к exchange 'logs'
и печатает все полученные сообщения.

Запуск (можно несколько параллельно):
    python 03_pubsub/receive_logs.py
"""

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

# exclusive=True — очередь удалится, когда consumer отключится.
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

print("[*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f"[x] {body.decode()}")


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True,
)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\n[!] Interrupted")
    try:
        sys.exit(0)
    except SystemExit:
        raise