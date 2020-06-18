# std lib
from os import getenv
from threading import Thread
import asyncio

# deps
from hypercorn.asyncio import serve
from hypercorn.config import Config
from loguru import logger           # type: ignore
from quart.exceptions import BadRequest
from quart import Quart, request
import discord                      # type: ignore


ENV = {var: getenv(var) or logger.warning(f"Env var {var} must be set")
       for var in ("DISCORD_TOKEN", "CHANNEL_ID")}


app: Quart = Quart(__name__)
bot = discord.Client()


@bot.event
async def on_ready():
    logger.info(f"{bot.user} has connected to Discord!")


@app.route("/sms", methods=["GET"])
async def sms_received():
    """ Webhook endpoint called by Twilio """
    # validate args
    text = await request.args.get("Body")
    sender = await request.args.get("From")
    assert type(sender) is str, BadRequest()
    assert type(text) is str, BadRequest()

    logger.info(f'Got "{text}" from {sender}, sending to discord!')

    # forward message to discord channel
    channel = bot.get_channel(ENV["CHANNEL_ID"])
    await channel.send(f"**{sender}** {text}")
    return "thank you", 200


if __name__ == "__main__":
    config = Config()
    config.bind = ["0.0.0.0:80"]
    # Start hypercorn and discord bot
    asyncio.run(asyncio.gather(serve(app, config),
                               bot.start(ENV["DISCORD_TOKEN"])))
