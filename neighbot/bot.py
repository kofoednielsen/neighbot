# std lib
from os import getenv
from threading import Thread
import asyncio

# deps
from quart import Quart    # type: ignore
import discord             # type: ignore
from loguru import logger  # type: ignore
from flask import Flask, request

TOKEN = getenv("DISCORD_TOKEN")
assert TOKEN, "Enrionment variable DISCORD_TOKEN must be set"

app: Quart = Quart(__name__)
client = discord.Client()

@app.before_first_request()
async def init_butt():
    @client.event
    async def on_ready():
        logger.info(f"{client.user} has connected to Discord!")

    asyncio.ensure_future(client.start(TOKEN))


@app.route("/sms", methods=["GET"])
async def sms_received():
    text = await request.args.get("Body")
    sender = await request.args.get("From")
    logger.info(f'Got "{text}" from {sender}, sending to discord!')
    for guild in client.guilds:
        for channel in guild.channels:
            if type(channel) is discord.TextChannel and channel.name == "neighbot":
                await channel.send(f"**{sender}** {text}")
    return "thank you", 200
