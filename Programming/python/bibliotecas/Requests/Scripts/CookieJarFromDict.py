"""Cria CookieJar a partir de um dicionário."""

import requests

cookies = {"usuario": "davi", "tema": "escuro"}
jar = requests.cookies.cookiejar_from_dict(cookies)
print(jar)
