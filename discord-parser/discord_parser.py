from loguru import logger
import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discord-bot")


def discord_parse(dont_need_this, not_this_either, nope_not_this, but_this_bytes):
    but_this = json.loads(but_this_bytes.decode("utf-8"))
    logger.info("Parsed discord-parse message and published discord-bot job")
    body = json.dumps(f"**{but_this[0]}** {but_this[1]}").encode("utf-8")
    channel.basic_publish(exchange="",
                          routing_key="discord-bot",
                          body=body)


channel.basic_consume("discord-parse", discord_parse, auto_ack=True)
channel.start_consuming()
