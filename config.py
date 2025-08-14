import discord
import nest_asyncio
import asyncio
import os
import requests

# Variáveis de ambiente
TOKEN = os.getenv("API_TOKEN")
CHANNEL_ID = 1405343780047159470

# Configuração do Discord
nest_asyncio.apply()
intents = discord.Intents.default()
client = discord.Client(intents=intents)
