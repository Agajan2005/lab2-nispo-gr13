"""
RabbitMQ Tutorial 1 — Hello World. Отправитель (producer).

Публикует одно сообщение "Hello World!" в очередь 'hello'.

Запуск (из каталога tutorials, с активированным venv):
    python 01_hello_world/send.py
"""

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)
channel = connection.channel()

channel.queue_declare(queue="hello", durable=False)

channel.basic_publish(
    exchange="",
    routing_key="hello",
    body="Hello World!",
)
print("[x] Sent 'Hello World!'")

connection.close()