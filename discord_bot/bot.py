from config import client, TOKEN, CHANNEL_ID, asyncio
from discord_bot.monitor import monitorar_criptomoeda

canal_discord = None

async def enviar_alerta_discord(mensagem):
    if canal_discord:
        await canal_discord.send(mensagem)
    else:
        print("Canal ainda não disponível.")

@client.event
async def on_ready():
    global canal_discord
    print(f'Logado como {client.user}')
    
    canal_discord = client.get_channel(CHANNEL_ID)
    if canal_discord:
        await canal_discord.send("Bot pronto para alertas de criptomoeda!")
        # Passa a função como argumento
        asyncio.create_task(monitorar_criptomoeda(enviar_alerta_discord))
    else:
        print("Canal não encontrado.")

async def iniciar_bot():
    await client.start(TOKEN)
