# Exemplos de Requests

Cada arquivo demonstra um recurso da biblioteca `requests`. Instale a dependência com `python -m pip install requests` e execute um exemplo com `python NomeDoScript.py`. Os exemplos usam `https://httpbin.org` e precisam de conexão com a internet.

## Requisições e parâmetros

- [`RequestsCookies.py`](./Scripts/RequestsCookies.py): Envia cookies ao servidor.
- [`RequestsData.py`](./Scripts/RequestsData.py): Envia campos de formulário no corpo da requisição.
- [`RequestsDelete.py`](./Scripts/RequestsDelete.py): Envia uma solicitação de exclusão.
- [`RequestsGet.py`](./Scripts/RequestsGet.py): Faz uma requisição GET e mostra status e texto.
- [`RequestsHead.py`](./Scripts/RequestsHead.py): Obtém status e cabeçalhos sem o corpo normal.
- [`RequestsHeaders.py`](./Scripts/RequestsHeaders.py): Define cabeçalhos HTTP personalizados.
- [`RequestsJson.py`](./Scripts/RequestsJson.py): Envia um objeto JSON.
- [`RequestsMethods.py`](./Scripts/RequestsMethods.py): Demonstra outros métodos com a função genérica request().
- [`RequestsParams.py`](./Scripts/RequestsParams.py): Adiciona parâmetros à URL.
- [`RequestsPatch.py`](./Scripts/RequestsPatch.py): Envia uma alteração parcial.
- [`RequestsPost.py`](./Scripts/RequestsPost.py): Envia dados JSON com POST.
- [`RequestsProxy.py`](./Scripts/RequestsProxy.py): Configura um proxy HTTP local.
- [`RequestsPut.py`](./Scripts/RequestsPut.py): Envia dados para criar ou substituir um recurso.
- [`RequestsRedirects.py`](./Scripts/RequestsRedirects.py): Controla e mostra redirecionamentos.
- [`RequestsRequest.py`](./Scripts/RequestsRequest.py): Usa request() para escolher o método HTTP.
- [`RequestsStream.py`](./Scripts/RequestsStream.py): Lê a resposta gradualmente, linha por linha.
- [`RequestsTimeout.py`](./Scripts/RequestsTimeout.py): Define o tempo máximo de espera.
- [`RequestsVerify.py`](./Scripts/RequestsVerify.py): Mantém a validação do certificado TLS/SSL.

## Respostas

- [`ResponseApparentEncoding.py`](./Scripts/ResponseApparentEncoding.py): Consulta a codificação estimada para o conteúdo.
- [`ResponseClose.py`](./Scripts/ResponseClose.py): Fecha explicitamente uma resposta em streaming.
- [`ResponseContent.py`](./Scripts/ResponseContent.py): Lê o corpo da resposta como bytes.
- [`ResponseCookies.py`](./Scripts/ResponseCookies.py): Exibe os cookies recebidos.
- [`ResponseElapsed.py`](./Scripts/ResponseElapsed.py): Mostra o tempo até a chegada dos cabeçalhos.
- [`ResponseEncoding.py`](./Scripts/ResponseEncoding.py): Lê e define a codificação do texto.
- [`ResponseHeaders.py`](./Scripts/ResponseHeaders.py): Consulta os cabeçalhos recebidos.
- [`ResponseHistory.py`](./Scripts/ResponseHistory.py): Mostra as respostas de redirecionamento anteriores.
- [`ResponseIterContent.py`](./Scripts/ResponseIterContent.py): Percorre o corpo em blocos de bytes.
- [`ResponseIterLines.py`](./Scripts/ResponseIterLines.py): Percorre uma resposta transmitida linha por linha.
- [`ResponseJson.py`](./Scripts/ResponseJson.py): Converte o corpo JSON em objeto Python.
- [`ResponseLinks.py`](./Scripts/ResponseLinks.py): Lê links do cabeçalho Link, se houver.
- [`ResponseOk.py`](./Scripts/ResponseOk.py): Verifica se o status indica ausência de erro HTTP.
- [`ResponseRaiseForStatus.py`](./Scripts/ResponseRaiseForStatus.py): Gera HTTPError quando o servidor retorna erro.
- [`ResponseReason.py`](./Scripts/ResponseReason.py): Mostra a descrição associada ao status HTTP.
- [`ResponseStatusCode.py`](./Scripts/ResponseStatusCode.py): Lê o código HTTP da resposta.
- [`ResponseText.py`](./Scripts/ResponseText.py): Lê o corpo da resposta como texto.
- [`ResponseUrl.py`](./Scripts/ResponseUrl.py): Mostra a URL final da resposta.

## Sessões e requisições preparadas

- [`PreparedRequest.py`](./Scripts/PreparedRequest.py): Inspeciona uma requisição POST preparada.
- [`RequestBuild.py`](./Scripts/RequestBuild.py): Constrói um objeto Request sem enviá-lo.
- [`RequestPrepare.py`](./Scripts/RequestPrepare.py): Prepara uma requisição e exibe seus campos.
- [`RequestsSession.py`](./Scripts/RequestsSession.py): Cria sessão e reutiliza conexões entre requisições.
- [`SendPreparedRequest.py`](./Scripts/SendPreparedRequest.py): Prepara e envia uma requisição com uma sessão.
- [`SessionAuth.py`](./Scripts/SessionAuth.py): Define autenticação básica na sessão.
- [`SessionCookies.py`](./Scripts/SessionCookies.py): Mantém cookies padrão na sessão.
- [`SessionHeaders.py`](./Scripts/SessionHeaders.py): Aplica cabeçalhos padrão a uma sessão.
- [`SessionMount.py`](./Scripts/SessionMount.py): Monta adaptador com tentativas de repetição.
- [`SessionOptions.py`](./Scripts/SessionOptions.py): Envia uma requisição OPTIONS usando uma sessão.
- [`SessionParams.py`](./Scripts/SessionParams.py): Aplica parâmetros padrão às requisições da sessão.

## Autenticação e cookies

- [`AuthBasic.py`](./Scripts/AuthBasic.py): Faz autenticação HTTP Basic.
- [`AuthCustom.py`](./Scripts/AuthCustom.py): Acrescenta um cabeçalho com autenticação personalizada.
- [`AuthDigest.py`](./Scripts/AuthDigest.py): Faz autenticação HTTP Digest.
- [`AuthProxy.py`](./Scripts/AuthProxy.py): Cria objeto de autenticação para proxy.
- [`CookieAddDict.py`](./Scripts/CookieAddDict.py): Adiciona um dicionário de cookies ao CookieJar.
- [`CookieDictFromJar.py`](./Scripts/CookieDictFromJar.py): Converte CookieJar em dicionário.
- [`CookieJarFromDict.py`](./Scripts/CookieJarFromDict.py): Cria CookieJar a partir de um dicionário.

## Utilidades e erros

- [`HttpCodes.py`](./Scripts/HttpCodes.py): Consulta códigos HTTP pelos nomes conhecidos.
- [`RequestsExceptions.py`](./Scripts/RequestsExceptions.py): Trata timeout, conexão, status e JSON inválido.
- [`UtilsEncodings.py`](./Scripts/UtilsEncodings.py): Encontra codificações declaradas no HTML.
- [`UtilsHeaderEncoding.py`](./Scripts/UtilsHeaderEncoding.py): Obtém codificação a partir dos cabeçalhos.
- [`UtilsUnicode.py`](./Scripts/UtilsUnicode.py): Obtém o conteúdo de resposta como texto Unicode.

## Arquivos, hooks e adaptadores

- [`DownloadFile.py`](./Scripts/DownloadFile.py): Baixa um arquivo e salva no diretório atual.
- [`DownloadStream.py`](./Scripts/DownloadStream.py): Baixa um arquivo em blocos para poupar memória.
- [`HttpAdapter.py`](./Scripts/HttpAdapter.py): Configura adaptador, pool e tentativas da sessão.
- [`ResponseHook.py`](./Scripts/ResponseHook.py): Executa uma função assim que a resposta chega.
- [`UploadFile.py`](./Scripts/UploadFile.py): Envia documento.txt como arquivo multipart.
