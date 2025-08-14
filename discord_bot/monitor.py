from datetime import datetime
from config import requests, asyncio

async def monitorar_criptomoeda(enviar_alerta):
    criptomoeda = "bitcoin"
    moeda_conversao = "brl"
    url_api = f"https://api.coingecko.com/api/v3/simple/price?ids={criptomoeda}&vs_currencies={moeda_conversao}"

    maior_valor = None
    menor_valor = None
    resultados = []

    while True:
        try:
            resposta = requests.get(url_api).json()
            valor_atual = resposta[criptomoeda][moeda_conversao]
            data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Novo maior valor
            if maior_valor is None or valor_atual > maior_valor:
                maior_valor = valor_atual
                mensagem = f"🚀 Novo MAIOR valor do Bitcoin: R$ {maior_valor:.2f} em {data_atual}"
                resultados.append(mensagem)
                print(mensagem)
                await enviar_alerta(mensagem)

            # Novo menor valor
            elif menor_valor is None or valor_atual < menor_valor:
                menor_valor = valor_atual
                diferenca = maior_valor - menor_valor
                percentual = (diferenca / maior_valor) * 100
                mensagem = (
                    f"📉 Novo MENOR valor do Bitcoin: R$ {menor_valor:.2f} em {data_atual}\n"
                    f"- Maior: R$ {maior_valor:.2f}\n"
                    f"- Queda: R$ {diferenca:.2f} ({percentual:.3f}%)"
                )
                resultados.append(mensagem)
                print(mensagem)
                await enviar_alerta(mensagem)

            # Valor está entre maior e menor
            else:
                diferenca = maior_valor - valor_atual
                percentual = (diferenca / maior_valor) * 100
                mensagem = (
                    f"📊 Valor atual: R$ {valor_atual:.2f} | "
                    f"Maior: R$ {maior_valor:.2f} | "
                    f"Menor: R$ {menor_valor:.2f} | "
                    f"Queda: R$ {diferenca:.2f} ({percentual:.2f}%)"
                )
                resultados.append(mensagem)
                print(mensagem)
                await enviar_alerta(mensagem)

            # Salva histórico em arquivo
            with open("valores.txt", "w", encoding="utf-8") as f:
                for item in resultados:
                    f.write(f"{item}\n")

            await asyncio.sleep(60)  # espera 1 minuto

        except Exception as e:
            print(f"Erro ao buscar preço: {e}")
            await asyncio.sleep(60)
