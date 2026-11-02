"""Trata timeout, conexão, status e JSON inválido."""

import requests

try:
    resposta = requests.get("https://httpbin.org/get", timeout=5)
    resposta.raise_for_status()
    print(resposta.json())
except requests.exceptions.Timeout:
    print("Tempo limite excedido.")
except requests.exceptions.ConnectionError:
    print("Problema de conexão.")
except requests.exceptions.HTTPError as erro:
    print("Erro HTTP:", erro)
except requests.exceptions.JSONDecodeError:
    print("Erro ao interpretar JSON.")
except requests.exceptions.RequestException as erro:
    print("Erro na requisição:", erro)
