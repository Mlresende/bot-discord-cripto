# 📈 Bot de Alerta de Criptomoeda no Discord

Este projeto é um **bot desenvolvido em Python** que se conecta a um canal do Discord e envia alertas em tempo real sobre o valor do Bitcoin em Reais (BRL), utilizando a API da [CoinGecko](https://www.coingecko.com/).

---

## 🚀 Funcionalidades

- Conexão automática com o canal do Discord especificado.
- Monitoramento do valor do Bitcoin a cada minuto.
- Alertas enviados quando:
  - O valor atual é o **maior registrado**.
  - Há uma **queda em relação ao maior valor**.
- Histórico de alertas salvo em `valores.txt`.
- Suporte para **execução contínua com asyncio**.

---

## 🧰 Tecnologias e Bibliotecas

- [discord.py](https://discordpy.readthedocs.io/en/stable/) – interação com o Discord.  
- [nest_asyncio](https://pypi.org/project/nest-asyncio/) – compatibilidade asyncio em ambientes que já possuem loop.  
- [requests](https://docs.python-requests.org/en/latest/) – requisições HTTP à API CoinGecko.  
- asyncio – gerenciamento de tarefas assíncronas.

---

## 🧱 Estrutura Modular

O projeto está organizado de forma modular para **facilitar manutenção e escalabilidade**:

cripto-moeda/<br>
│<br>
├── main.py # Ponto de entrada do bot<br>
├── config.py # Configurações e variáveis de ambiente<br>
├── discord_bot/<br>
│ ├── init.py<br>
│ ├── bot.py # Inicialização e eventos do Discord<br>
│ └── monitor.py # Lógica de monitoramento da criptomoeda<br>
└── valores.txt # Histórico de alertas


### Como funciona a modularização:

- **bot.py**: Inicializa o client do Discord, gerencia eventos e envia alertas.  
- **monitor.py**: Contém a lógica de monitoramento do Bitcoin e envio de mensagens via função passada como argumento.  
- **config.py**: Centraliza variáveis de ambiente e configurações (TOKEN, CHANNEL_ID, imports comuns).  
- **valores.txt**: Armazena o histórico dos alertas enviados.  

Essa estrutura permite facilmente:
- Monitorar outras criptomoedas.
- Adicionar integração com outras plataformas.
- Separar responsabilidades do código, mantendo o projeto organizado.

---

## ⚡ Execução

1. Crie um **ambiente virtual** e instale as dependências:
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
