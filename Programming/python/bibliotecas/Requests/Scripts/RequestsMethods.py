"""Demonstra outros métodos com a função genérica request()."""

import requests

# O mesmo método genérico também envia outros verbos HTTP.
for metodo in ("POST", "PUT", "PATCH", "DELETE"):
    resposta = requests.request(metodo, f"https://httpbin.org/{metodo.lower()}", timeout=10)
    print(metodo, resposta.status_code)
