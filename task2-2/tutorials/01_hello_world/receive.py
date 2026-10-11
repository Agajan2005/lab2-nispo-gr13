"""
RabbitMQ Tutorial 1 — Hello World. Получатель (consumer).

Слушает очередь 'hello' и печатает каждое полученное сообщение.

Запуск:
    python 01_hello_world/receive.py
"""

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)
channel = connection.channel()

channel.queue_declare(queue="hello", durable=False)


def callback(ch, method, properties, body):
    print(f"[x] Received {body.decode()}")


channel.basic_consume(
    queue="hello",
    on_message_callback=callback,
    auto_ack=True,
)

print("[*] Waiting for messages. To exit press CTRL+C")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\n[!] Interrupted")
    try:
        sys.exit(0)
    except SystemExit:
        raise