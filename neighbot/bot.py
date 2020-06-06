# deps
from os import getenv
from loguru import logger
from flask import Flask, request
from threading import Thread
import discord
import asyncio

TOKEN = getenv('DISCORD_TOKEN')
assert TOKEN, "Enrionment variable DISCORD_TOKEN must be set"
logger.info(f'TOKEN is "{TOKEN}"')

client = discord.Client()
app = Flask(__name__)


def run_it_forever(loop):
    loop.run_forever()


def start_bot():
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(TOKEN))

    thread = Thread(target=run_it_forever, args=(loop,))
    thread.start()


@client.event
async def on_ready():
    logger.info(f'{client.user} has connected to Discord!')


@app.route("/sms", methods=['GET'])
def sms_received():
    text = request.args.get('Body')
    logger.info(f'Received message "{text}", now sending it to discord')
    for guild in client.guilds:
        logger.info(f'client is in guild "{guild.name}"')
        for channel in guild.channels:
            if type(channel) is discord.TextChannel:
                logger.info(f'Send message to channel "{channel.name}"')
                asyncio.run_coroutine_threadsafe(channel.send(text), client.loop)
    return 'thank you', 200


start_bot()
