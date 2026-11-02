"""Obtém o conteúdo de resposta como texto Unicode."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
texto = requests.utils.get_unicode_from_response(resposta)
print(texto)
