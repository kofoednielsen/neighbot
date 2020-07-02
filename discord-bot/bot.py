import discord  # type: ignore
import pika  # type: ignore
import loguru  # type: ignore
from os import environ

# setup rabbitmq shit
connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discordbot")

# discord shit
bot = discord.Client()


@bot.event
async def on_ready():
    logger.info(f"{client.user} has connected to Discord!")


def send_to_discord(ch, method, properties, body):
    # forward message to discord channel
    logger.info(f"Sending to discord: {body}")
    channel = bot.get_channel(environ["CHANNEL_ID"])
    channel.send(body)


if __name__ == "__main__":
    channel.basic_consume(
        queue="discordbot", on_message_callback=send_to_discord, auto_ack=True
    )
    channel.start_consuming()
