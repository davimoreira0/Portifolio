"""Executa uma função assim que a resposta chega."""

import requests

def meu_hook(resposta, *args, **kwargs):
    print("Resposta recebida!", resposta.status_code)
    return resposta

resposta = requests.get("https://httpbin.org/get", hooks={"response": meu_hook}, timeout=10)
print(resposta.text)
