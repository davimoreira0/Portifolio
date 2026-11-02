"""Inspeciona uma requisição POST preparada."""

import requests

requisicao = requests.Request("POST", "https://httpbin.org/post", json={"nome": "Davi"})
preparada = requisicao.prepare()
print(preparada.method)
print(preparada.url)
print(preparada.body)
