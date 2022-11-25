import discord
from decouple import config
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

# evento executado ao rodar arquivo
@bot.event
async def on_ready():
    print("Conectado!")
    await bot.load_extension("manager")
    await bot.load_extension("commands.talks")

# token do bot
TOKEN = config("TOKEN")
bot.run(TOKEN)
