import discord  # type: ignore
import pika  # type: ignore
from loguru import logger # type: ignore
from os import environ
from threading import Thread

# setup rabbitmq shit
connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discordbot")
                                       #  ░█▀▄░█▀█░█▀█░█▀█
# discord shit                         #  ░█▀▄░█░█░█░█░█▀▀
bot = discord.Client()                 #  ░▀▀░░▀▀▀░▀▀▀░▀░░

def send_to_discord(ch, method, properties, body):
    # forward message to discord channel
    print(f"Sending to discord: {body}")
    bot.get_channel(environ["CHANNEL_ID"]).send(body)

def start_consumer():
    channel.basic_consume(queue="discordbot", on_message_callback=send_to_discord, auto_ack=True)
    channel.start_consuming()

def start_discord_bot():
    bot.run(environ["DISCORD_TOKEN"])

if __name__ == "__main__":
    Thread(target=start_discord_bot).start()
    start_consumer()
