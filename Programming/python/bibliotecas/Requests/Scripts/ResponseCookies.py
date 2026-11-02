"""Exibe os cookies recebidos."""

import requests

resposta = requests.get("https://httpbin.org/cookies/set/teste/123", timeout=10)
print(resposta.cookies)
