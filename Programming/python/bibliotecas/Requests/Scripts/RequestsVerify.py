"""Mantém a validação do certificado TLS/SSL."""

import requests

# A validação é ativada por padrão; mantenha verify=True.
resposta = requests.get("https://httpbin.org/get", verify=True, timeout=10)
print(resposta.status_code)
