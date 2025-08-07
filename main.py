# bot_discord.py
import discord
import nest_asyncio
import asyncio
import os

TOKEN = os.getenv(API_TOKEN)  # Substitua pelo novo token seguro
CHANNEL_ID = 1402797286869831710

nest_asyncio.apply()
intents = discord.Intents.default()
client = discord.Client(intents=intents)

canal_discord = None

@client.event
async def on_ready():
    global canal_discord
    print(f'Logado como {client.user}')
    
    canal_discord = client.get_channel(CHANNEL_ID)
    if canal_discord:
        await canal_discord.send("Bot pronto para alertas de criptomoeda!")
        asyncio.create_task(monitorar_criptomoeda())  # iniciar aqui
    else:
        print("Canal não encontrado.")

async def enviar_alerta_discord(mensagem):
    if canal_discord:
        await canal_discord.send(mensagem)
    else:
        print("Canal ainda não disponível.")

async def monitorar_criptomoeda():
    import requests
    from datetime import datetime

    criptomoeda = "bitcoin"
    moeda_conversao = "brl"
    url_api = f"https://api.coingecko.com/api/v3/simple/price?ids={criptomoeda}&vs_currencies={moeda_conversao}"

    maior_valor = None
    resultados = []

    while True:
        try:
            resposta = requests.get(url_api).json()
            valor_atual = resposta[criptomoeda][moeda_conversao]
            data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if maior_valor is None or valor_atual > maior_valor:
                maior_valor = valor_atual
                mensagem = f"🚀 Novo MAIOR valor do Bitcoin: R$ {maior_valor:.2f} em {data_atual}"
                resultados.append(mensagem)
                print(mensagem)
                await enviar_alerta_discord(mensagem)
            else:
                diferenca = maior_valor - valor_atual
                percentual = (diferenca / maior_valor) * 100
                if percentual >= 0:
                    mensagem = (
                        f"📉 Valor atual: R$ {valor_atual:.2f} | "
                        f"Maior: R$ {maior_valor:.2f} | "
                        f"Queda: R$ {diferenca:.2f} ({percentual:.2f}%)"
                    )
                    print(mensagem)
                    await enviar_alerta_discord(mensagem)
                else:
                    print("Preço se manteve o mesmo")

            with open("valores.txt", "w", encoding="utf-8") as f:
                for item in resultados:
                    f.write(f"{item}\n")

            await asyncio.sleep(60)

        except Exception as e:
            print(f"Erro: {e}")
            await asyncio.sleep(60)

async def main():
    await client.start(TOKEN)

asyncio.run(main())
