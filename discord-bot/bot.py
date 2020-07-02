import discord  # type: ignore                   
import pika  # type: ignore                      # ░█▀▀░█▀█░▀█▀░█▀▄░█▀█
from loguru import logger # type: ignore         # ░█▀▀░█░█░░█░░█▀▄░█▀▀
from os import environ                           # ░▀░░░▀░▀░▀▀▀░▀░▀░▀░░
from threading import Thread                     

# setup rabbitmq shit
connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))    #   ____________ 
channel = connection.channel()                                             #  < SLIP FNAPB >
channel.queue_declare(queue="discordbot")                                  #   ------------ 
                                       #  ░█▀▄░█▀█░█▀█░█▀█                 #     \
# discord shit                         #  ░█▀▄░█░█░█░█░█▀▀                 #      \
bot = discord.Client()                 #  ░▀▀░░▀▀▀░▀▀▀░▀░░                 #          .--.
                                                                           #         |o_o |
def send_to_discord(ch, method, properties, body_bytes):                   #         |:_/ |
    # decode body
    body = body_bytes.decode("utf-8")
    # forward message to discord channel                                   #        //   \ \
    print(f"Sending to discord: {body}")                                   #       (|     | )
    bot.get_channel(environ["CHANNEL_ID"]).send(body)                      #      /'\_   _/`\
                                                                           #      \___)=(___/
def start_consumer():
    channel.basic_consume(queue="discordbot", on_message_callback=send_to_discord, auto_ack=True)
    channel.start_consuming()

def start_discord_bot():                      #   ______________ 
    bot.run(environ["DISCORD_TOKEN"])         #  < FLAP BLAPNAP >
                                              #   -------------- 
if __name__ == "__main__":                    #         \   ^__^
    Thread(target=start_discord_bot).start()  #          \  (oo)\_______
    start_consumer()                          #             (__)\       )\/\
                                              #                  ||----w |
                                              #                  ||     ||
