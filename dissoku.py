from discord import client
import bump
from config import pepper
from config import token
import discord
client = discord.Client()


@client.event
async def on_message(message):
    await bump.bot_observer(message=message, pepper=pepper['dissoku'])


client.run(token)
