"""Define cabeçalhos HTTP personalizados."""

import requests

# headers personaliza os metadados enviados.
cabecalhos = {"User-Agent": "MeuProgramaPython/1.0", "Accept": "application/json"}
resposta = requests.get("https://httpbin.org/headers", headers=cabecalhos, timeout=10)
print(resposta.json())
