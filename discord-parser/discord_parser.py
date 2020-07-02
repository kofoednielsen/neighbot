from loguru import logger
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discord-bot")


def discord_parse(dont_need_this, not_this_either, nope_not_this, but_this):
    logger.info("Parsed discord-parse message and published discord-bot job")
    channel.basic_publish(exchange="",
                          routing_key="discord-parse",
                          body=f"**{but_this[0]}** {but_this[1]}")


channel.basic_consume("discord-parse", discord_parse)
channel.start_consuming()
