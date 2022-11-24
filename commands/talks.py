from discord.ext import commands

class Talks(commands.Cog):
    """ Talks with user """
    def __init__(self, bot):
        self.bot = bot
        
    # !oi
    @bot.command(name="oi", help="Envia um oi (não requer argumento)")
    async def send_hello(ctx):
        name = ctx.author.name
        
        response = "Olá, " + name
        
        await ctx.send(response)
        
def setup(bot):
    bot.add_cog(Talks(bot))
        