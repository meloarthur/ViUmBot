import discord
from discord.ext import commands

class Talks(commands.Cog):
    """ Talks with user """
    
    def __init__(self, bot):
        self.bot = bot
        
    # !oi
    @commands.command(name="oi", help="Envia um oi (não requer argumento)")
    async def send_hello(self, ctx):
        name = ctx.author.name
        
        response = f"Olá, " + name
        
        await ctx.send(response)
        
    # !regras
    @commands.command(name="regras")
    async def rules(self, ctx):
        response = """
    :robot::warning:REGRAS DO SERVIDOR:warning::robot:
        
:one: Trate todos com respeito. Nenhum tipo de assédio, caça às bruxas, sexismo, racismo ou discurso de ódio será tolerado.
:two: É proibido fazer spam ou autopromoção (convites de servidor, anúncios, etc) sem permissão de um membro da equipe. Isso inclui mandar Dms para outros membros.
:three: Nada de conteúdo com restrição de idade ou obsceno. Isso inclui texto, imagens ou links que contenham nudez, sexo, violência pesada ou conteúdo graficamente perturbador.
:four: Se você vir algo que quebre as regras, ou algo que te faça sentir insegurança, avise a equipe. Queremos que este servidor seja um espaço acolhedor!
        """
        
        await ctx.send(response)
    
    # !segredo
    @commands.command(name="segredo", help="Envia um segredo no privado (não requer argumento)")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Ei, psiu!")
            await ctx.author.send("Siga nossa página do Twitter @ViUmaVaga :ballot_box_with_check:")
            await ctx.author.send("Assine nossa newsletter :ballot_box_with_check:")
            await ctx.author.send("Convide alguém para nossa comunidade :ballot_box_with_check:")
            await ctx.author.send("Espalhe esse segredo... :face_with_hand_over_mouth:")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")
    
        
async def setup(bot):
    await bot.add_cog(Talks(bot))
        