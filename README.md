# 📈 Bot de Alerta de Criptomoeda no Discord

Este projeto é um bot desenvolvido em Python que se conecta a um canal do Discord e envia alertas sobre o valor do **Bitcoin** em tempo real, utilizando a API da [CoinGecko](https://www.coingecko.com/).

## 🚀 Funcionalidades

- Conecta-se automaticamente ao canal do Discord especificado.
- Monitora o valor do Bitcoin em reais (BRL) a cada minuto.
- Envia alertas quando:
  - O valor atual é o maior registrado.
  - Há uma queda em relação ao maior valor.
- Salva os alertas em um arquivo `valores.txt`.

## 🧰 Tecnologias e Bibliotecas

- [discord.py](https://github.com/Rapptz/discord.py)
- [nest_asyncio](https://pypi.org/project/nest-asyncio/)
- [requests](https://docs.python-requests.org/en/latest/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)

## 🧱 Modularização futura
Este projeto será modularizado em breve para melhorar a organização e facilitar a manutenção. A ideia é dividir o código em:

bot.py: inicialização e eventos do Discord.

monitor.py: lógica de monitoramento da criptomoeda.

utils.py: funções auxiliares (como salvar em arquivo).

config.py: variáveis de ambiente e configurações.

Essa estrutura tornará o projeto mais escalável e pronto para receber novas funcionalidades, como monitoramento de outras moedas ou integração com diferentes plataformas.
