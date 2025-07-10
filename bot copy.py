import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "oi":
        await message.channel.send(f"Oi, {message.author.display_name}!")
                
bot.run(TOKEN)