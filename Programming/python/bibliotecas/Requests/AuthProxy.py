"""Cria objeto de autenticação para proxy."""

import requests

autenticacao = requests.auth.HTTPProxyAuth("usuario", "senha")
print(autenticacao)
