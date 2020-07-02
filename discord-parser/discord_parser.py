from loguru import logger
import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discord-bot")


def discord_parse(dont_need_this, not_this_either, nope_not_this, but_this):
    but_this = json.loads(but_this.decode("utf-8"))
    logger.info("Parsed discord-parse message and published discord-bot job")
    body = f"**{but_this[0]}** {but_this[1]}".encode("utf-8")
    channel.basic_publish(exchange="",
                          routing_key="discord-parse",
                          body=body)


channel.basic_consume("discord-parse", discord_parse)
channel.start_consuming()
