# deps
from os import getenv
from loguru import logger
import discord

TOKEN = getenv('DISCORD_TOKEN')

assert TOKEN, "Enrionment variable DISCORD_TOKEN must be set"

logger.info(f'TOKEN is "{TOKEN}"')

client = discord.Client()


@client.event
async def on_ready():
    logger.info(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        logger.info(f'client is in guild "{guild.name}"')
        for channel in guild.channels:
            if type(channel) is discord.TextChannel:
                logger.info(f'Send message to channel "{channel.name}"')
                await channel.send('Hello, im a bot!')

client.run(TOKEN)
