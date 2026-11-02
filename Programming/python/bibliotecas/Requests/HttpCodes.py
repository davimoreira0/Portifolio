"""Consulta códigos HTTP pelos nomes conhecidos."""

import requests

print(requests.codes.ok)
print(requests.codes.created)
print(requests.codes.not_found)
print(requests.codes.forbidden)
print(requests.codes.internal_server_error)
print(requests.codes["teapot"])
