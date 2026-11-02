"""Faz autenticação HTTP Digest."""

import requests

autenticacao = requests.auth.HTTPDigestAuth("usuario", "senha")
resposta = requests.get("https://httpbin.org/digest-auth/auth/usuario/senha", auth=autenticacao, timeout=10)
print(resposta.status_code)
