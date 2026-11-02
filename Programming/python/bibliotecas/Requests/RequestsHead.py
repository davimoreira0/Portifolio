"""Obtém status e cabeçalhos sem o corpo normal."""

import requests

# HEAD retorna metadados da resposta.
resposta = requests.head("https://httpbin.org/get", timeout=10)
print(resposta.status_code)
print(resposta.headers)
