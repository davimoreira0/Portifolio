"""Controla e mostra redirecionamentos."""

import requests

# allow_redirects habilita o seguimento automático.
resposta = requests.get("https://httpbin.org/redirect/1", allow_redirects=True, timeout=10)
print(resposta.url)
print(resposta.history)
