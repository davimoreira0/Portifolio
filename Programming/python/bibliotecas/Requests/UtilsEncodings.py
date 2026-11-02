"""Encontra codificações declaradas no HTML."""

import requests

html = '<html><head><meta charset="utf-8"></head></html>'
print(requests.utils.get_encodings_from_content(html))
