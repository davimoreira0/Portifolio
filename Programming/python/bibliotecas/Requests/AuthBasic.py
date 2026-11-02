"""Faz autenticação HTTP Basic."""

import requests

autenticacao = requests.auth.HTTPBasicAuth("usuario", "senha")
resposta = requests.get("https://httpbin.org/basic-auth/usuario/senha", auth=autenticacao, timeout=10)
print(resposta.status_code)
