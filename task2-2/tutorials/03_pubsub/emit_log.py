"""
RabbitMQ Tutorial 3 — Publish/Subscribe. Издатель.

Публикует сообщения в exchange типа 'fanout' с именем 'logs'.
Все подписанные очереди получат копию каждого сообщения.

Запуск:
    python 03_pubsub/emit_log.py "Сообщение лога"
"""

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)
channel = connection.channel()

# Exchange типа fanout — рассылает копию сообщения во все привязанные очереди.
channel.exchange_declare(exchange="logs", exchange_type="fanout")

message = " ".join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(
    exchange="logs",
    routing_key="",  # для fanout не важен
    body=message,
)
print(f"[x] Sent {message!r}")

connection.close()