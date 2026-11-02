"""Converte CookieJar em dicionário."""

import requests

jar = requests.cookies.cookiejar_from_dict({"usuario": "davi"})
dados = requests.utils.dict_from_cookiejar(jar)
print(dados)
