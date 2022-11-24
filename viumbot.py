import datetime
import discord
from discord.ext import commands, tasks

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

# evento executado ao rodar arquivo
@bot.event
async def on_ready():
    print("Conectado!")
    current_time.start()
    
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
    
# !oi
@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    
    response = "Olá, " + name
    
    await ctx.send(response)
    
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
    
# data-hora (a cada 10 segundos)
@tasks.loop(seconds=10)
async def current_time():
    now = datetime.datetime.now()
    
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    
    channel = bot.get_channel(1045158430199001151)
    
    await channel.send("Data atual: " + now)

# token do bot
bot.run('MTA0NTE1MDAwMjA4OTA0MTk2MQ.GwJG1Z.ApvTcCL_tNtgvcn2QzxarEpX3KTxbDoz3TKlpM')
