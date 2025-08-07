#!/bin/bash

echo "Instalando Python..."
# No Linux, geralmente Python já vem instalado, mas para instalar via apt (Debian/Ubuntu):
sudo apt update
sudo apt install -y python3 python3-venv python3-pip

echo "Criando ambiente virtual..."
python3 -m venv .venv_cripto

echo "Ativando ambiente virtual..."
source .venv_cripto/bin/activate

echo "Instalando bibliotecas utilizadas na aplicacao Crypto-Moeda..."
pip install requests pywhatkit discord nest_asyncio asyncio

echo "Pronto!"
