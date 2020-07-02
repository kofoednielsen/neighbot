import discord  # type: ignore                   
import pika  # type: ignore                      # ░█▀▀░█▀█░▀█▀░█▀▄░█▀█
import asyncio
from loguru import logger # type: ignore         # ░█▀▀░█░█░░█░░█▀▄░█▀▀
from os import getenv                            # ░▀░░░▀░▀░▀▀▀░▀░▀░▀░░
from threading import Thread                     

# setup rabbitmq shit
connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))    #   ____________ 
channel = connection.channel()                                             #  < SLIP FNAPB >
                                       #  ░█▀▄░█▀█░█▀█░█▀█                 #     \
# discord shit                         #  ░█▀▄░█░█░█░█░█▀▀                 #      \
bot = discord.Client()                 #  ░▀▀░░▀▀▀░▀▀▀░▀░░                 #          .--.
                                                                           #         |o_o |

def send_to_discord(ch, method, properties, body_bytes):                   #         |:_/ |
    # decode body
    body = body_bytes.decode("utf-8")
    # forward message to discord channel                                   #        //   \ \
    print(f"Sending to discord: {body}")                                   #       (|     | )
    for guild in bot.guilds:
        for channel in guild.channels:
            if type(channel) is discord.TextChannel and channel.name == "debug":
                asyncio.run_coroutine_threadsafe(channel.send(body), client.loop)
                return
    logger.error("DIDNT FIND DISCROD CHANELLES FUCK ")
                                                                           #      \___)=(___/

def start_consumer():
    channel.basic_consume(queue="discord-bot", on_message_callback=send_to_discord, auto_ack=True)
    channel.start_consuming()

def start_discord_bot():                      #   ______________ 
    bot.run(getenv("DISCORD_TOKEN"))         #  < FLAP BLAPNAP >
                                              #   -------------- 
if __name__ == "__main__":                    #         \   ^__^
    Thread(target=start_discord_bot).start()  #          \  (oo)\_______
    start_consumer()                          #             (__)\       )\/\
                                              #                  ||----w |
                                              #                  ||     ||
