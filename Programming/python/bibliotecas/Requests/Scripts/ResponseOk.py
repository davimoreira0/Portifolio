"""Verifica se o status indica ausência de erro HTTP."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
if resposta.ok:  # True para status abaixo de 400.
    print("Requisição realizada sem erro HTTP.")
else:
    print("O servidor retornou um erro HTTP.")
