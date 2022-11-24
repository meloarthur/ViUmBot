import datetime
import discord
import os
from decouple import config
from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

# evento executado ao rodar arquivo
@bot.event
async def on_ready():
    print("Conectado!")
    
# boas vindas
@bot.event
async def on_member_join(member):
    boas_vindas = bot.get_channel(938929140403433574)
    regras = bot.get_channel(1041816946091511840),
    se_apresenta_ai = bot.get_channel(1041828611273019452)
    chat_geral = bot.get_channel(1041816946280239168)
    parcerias = bot.get_channel(1042494940279750707)
    pets = bot.get_channel(1042446806098907276)
    games = bot.get_channel(1042414084219478147)
    estudos = bot.get_channel(1041832446326493254)
    
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
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Favor enviar todos os argumentos. Digite !help para ver os parâmetros de cada comando.")
    if isinstance(error, CommandNotFound):
        await ctx.send("O comando não existe... Digite !help para ver todos os comandos!")
    else:
        raise error
    
# !regras
@bot.command(name="regras")
async def rules(ctx):
    response = """
   :robot::warning:REGRAS DO SERVIDOR:warning::robot:
    
:one: Trate todos com respeito. Nenhum tipo de assédio, caça às bruxas, sexismo, racismo ou discurso de ódio será tolerado.
:two: É proibido fazer spam ou autopromoção (convites de servidor, anúncios, etc) sem permissão de um membro da equipe. Isso inclui mandar Dms para outros membros.
:three: Nada de conteúdo com restrição de idade ou obsceno. Isso inclui texto, imagens ou links que contenham nudez, sexo, violência pesada ou conteúdo graficamente perturbador.
:four: Se você vir algo que quebre as regras, ou algo que te faça sentir insegurança, avise a equipe. Queremos que este servidor seja um espaço acolhedor!
    """
    
    await ctx.send(response)
  
# !segredo
@bot.command(name="segredo", help="Envia um segredo no privado (não requer argumento)")
async def secret(ctx):
    try:
        await ctx.author.send("Ei, psiu!")
        await ctx.author.send("Siga nossa página do Twitter @ViUmaVaga :ballot_box_with_check:")
        await ctx.author.send("Assine nossa newsletter :ballot_box_with_check:")
        await ctx.author.send("Convide alguém para nossa comunidade :ballot_box_with_check:")
        await ctx.author.send("Espalhe esse segredo... :face_with_hand_over_mouth:")
    except discord.errors.Forbidden:
        await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")
    
# verifica palavrões
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "palavrão" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, não ofenda os demais usuários!"
        )
        
        await message.delete()
        
    await bot.process_commands(message)

# token do bot
TOKEN = config("TOKEN")
bot.run(TOKEN)
