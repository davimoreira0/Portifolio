"""Fecha explicitamente uma resposta em streaming."""

import requests

resposta = requests.get("https://httpbin.org/get", stream=True, timeout=10)
print(resposta.status_code)
resposta.close()
