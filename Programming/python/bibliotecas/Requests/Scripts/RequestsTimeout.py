"""Define o tempo máximo de espera."""

import requests

# timeout evita que a execução espere indefinidamente.
resposta = requests.get("https://httpbin.org/delay/2", timeout=5)
print(resposta.status_code)
# Também se pode separar conexão e leitura: timeout=(3, 10).
