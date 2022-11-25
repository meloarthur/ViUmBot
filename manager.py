from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

class Manager(commands.Cog):
    """ Manage the boot """
    
    def __init__(self, bot):
        self.bot = bot
        
    # boas vindas
    @commands.Cog.listener()
    async def on_member_join(self, member):
        boas_vindas = self.bot.get_channel(938929140403433574)
        regras = self.bot.get_channel(1041816946091511840),
        se_apresenta_ai = self.bot.get_channel(1041828611273019452)
        chat_geral = self.bot.get_channel(1041816946280239168)
        parcerias = self.bot.get_channel(1042494940279750707)
        pets = self.bot.get_channel(1042446806098907276)
        games = self.bot.get_channel(1042414084219478147)
        estudos = self.bot.get_channel(1041832446326493254)
        
        message = f"""
        Salve, {member.mention}! Bem-vindo(a) ao ViUmaVagaVerso! :lori_happy:
        
A comunidade do ViUmaVagaVerso tem como objetivo ser um local seguro e amistoso, onde juntos possamos aprender, nos desenvolver e criarmos novos amigos!
    
E todas as pessoas são muito bem vindas aqui!
    
• Leia as {regras.mention} para você poder conviver em harmonia! :blobheart:
• Se apresente no {se_apresenta_ai.mention} , conta pra a gente mais sobre você, seus hobbies, de onde você é, idade, e quais tecnologias gosta/trabalha.
• Bora trocar uma ideia no canal de {chat_geral.mention} :lori_pac:
• Lá em {parcerias.mention} você fica por dentro dos descontos, cupons e benefícios por participar da nossa comunidade! Fique sempre de olho!
• Interaja com a galera, faça amigos, poste foto dos seus pets em {pets.mention}, fale dos jogos que você gosta em {games.mention}, do que está estudando em {estudos.mention}, e navegue por todos os demais canais que temos por aqui!
• E é claro, divirta-se, vamos nessa juntos! :emojo_feriado:

Ah, e se você quiser ficar por dentro de tudo que rola no ViUmaVagaVerso:
• Nos siga no Instagram: https://instagram.com/viumavaga
• E assine nossa newsletter, tá cheio de conteúdo bacana por lá!

Aqui você encontra o link de todas as nossas redes, newsletter, e etc: https://linklist.bio/viumavaga
        """
        
        await boas_vindas.send(message)
    
    # verifica comandos errados
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite !help para ver os parâmetros de cada comando.")
        if isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe... Digite !help para ver todos os comandos!")
        else:
            raise error
        
    # verifica palavrões
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if "palavrão" in message.content:
            await message.channel.send(
                f"Por favor, {message.author.name}, não ofenda os demais usuários!"
            )
            
            await message.delete()
        
async def setup(bot):
    await bot.add_cog(Manager(bot))
        