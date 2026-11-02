"""Adiciona um dicionário de cookies ao CookieJar."""

import requests

jar = requests.cookies.RequestsCookieJar()
requests.utils.add_dict_to_cookiejar(jar, {"usuario": "davi", "idioma": "portugues"})
print(jar)
