# Exemplos de Requests

Cada arquivo demonstra um recurso da biblioteca `requests`. Instale a dependência com `python -m pip install requests` e execute um exemplo com `python NomeDoScript.py`. Os exemplos usam `https://httpbin.org` e precisam de conexão com a internet.

## Requisições e parâmetros

- [`RequestsCookies.py`](./RequestsCookies.py): Envia cookies ao servidor.
- [`RequestsData.py`](./RequestsData.py): Envia campos de formulário no corpo da requisição.
- [`RequestsDelete.py`](./RequestsDelete.py): Envia uma solicitação de exclusão.
- [`RequestsGet.py`](./RequestsGet.py): Faz uma requisição GET e mostra status e texto.
- [`RequestsHead.py`](./RequestsHead.py): Obtém status e cabeçalhos sem o corpo normal.
- [`RequestsHeaders.py`](./RequestsHeaders.py): Define cabeçalhos HTTP personalizados.
- [`RequestsJson.py`](./RequestsJson.py): Envia um objeto JSON.
- [`RequestsMethods.py`](./RequestsMethods.py): Demonstra outros métodos com a função genérica request().
- [`RequestsParams.py`](./RequestsParams.py): Adiciona parâmetros à URL.
- [`RequestsPatch.py`](./RequestsPatch.py): Envia uma alteração parcial.
- [`RequestsPost.py`](./RequestsPost.py): Envia dados JSON com POST.
- [`RequestsProxy.py`](./RequestsProxy.py): Configura um proxy HTTP local.
- [`RequestsPut.py`](./RequestsPut.py): Envia dados para criar ou substituir um recurso.
- [`RequestsRedirects.py`](./RequestsRedirects.py): Controla e mostra redirecionamentos.
- [`RequestsRequest.py`](./RequestsRequest.py): Usa request() para escolher o método HTTP.
- [`RequestsStream.py`](./RequestsStream.py): Lê a resposta gradualmente, linha por linha.
- [`RequestsTimeout.py`](./RequestsTimeout.py): Define o tempo máximo de espera.
- [`RequestsVerify.py`](./RequestsVerify.py): Mantém a validação do certificado TLS/SSL.

## Respostas

- [`ResponseApparentEncoding.py`](./ResponseApparentEncoding.py): Consulta a codificação estimada para o conteúdo.
- [`ResponseClose.py`](./ResponseClose.py): Fecha explicitamente uma resposta em streaming.
- [`ResponseContent.py`](./ResponseContent.py): Lê o corpo da resposta como bytes.
- [`ResponseCookies.py`](./ResponseCookies.py): Exibe os cookies recebidos.
- [`ResponseElapsed.py`](./ResponseElapsed.py): Mostra o tempo até a chegada dos cabeçalhos.
- [`ResponseEncoding.py`](./ResponseEncoding.py): Lê e define a codificação do texto.
- [`ResponseHeaders.py`](./ResponseHeaders.py): Consulta os cabeçalhos recebidos.
- [`ResponseHistory.py`](./ResponseHistory.py): Mostra as respostas de redirecionamento anteriores.
- [`ResponseIterContent.py`](./ResponseIterContent.py): Percorre o corpo em blocos de bytes.
- [`ResponseIterLines.py`](./ResponseIterLines.py): Percorre uma resposta transmitida linha por linha.
- [`ResponseJson.py`](./ResponseJson.py): Converte o corpo JSON em objeto Python.
- [`ResponseLinks.py`](./ResponseLinks.py): Lê links do cabeçalho Link, se houver.
- [`ResponseOk.py`](./ResponseOk.py): Verifica se o status indica ausência de erro HTTP.
- [`ResponseRaiseForStatus.py`](./ResponseRaiseForStatus.py): Gera HTTPError quando o servidor retorna erro.
- [`ResponseReason.py`](./ResponseReason.py): Mostra a descrição associada ao status HTTP.
- [`ResponseStatusCode.py`](./ResponseStatusCode.py): Lê o código HTTP da resposta.
- [`ResponseText.py`](./ResponseText.py): Lê o corpo da resposta como texto.
- [`ResponseUrl.py`](./ResponseUrl.py): Mostra a URL final da resposta.

## Sessões e requisições preparadas

- [`PreparedRequest.py`](./PreparedRequest.py): Inspeciona uma requisição POST preparada.
- [`RequestBuild.py`](./RequestBuild.py): Constrói um objeto Request sem enviá-lo.
- [`RequestPrepare.py`](./RequestPrepare.py): Prepara uma requisição e exibe seus campos.
- [`RequestsSession.py`](./RequestsSession.py): Cria sessão e reutiliza conexões entre requisições.
- [`SendPreparedRequest.py`](./SendPreparedRequest.py): Prepara e envia uma requisição com uma sessão.
- [`SessionAuth.py`](./SessionAuth.py): Define autenticação básica na sessão.
- [`SessionCookies.py`](./SessionCookies.py): Mantém cookies padrão na sessão.
- [`SessionHeaders.py`](./SessionHeaders.py): Aplica cabeçalhos padrão a uma sessão.
- [`SessionMount.py`](./SessionMount.py): Monta adaptador com tentativas de repetição.
- [`SessionOptions.py`](./SessionOptions.py): Envia uma requisição OPTIONS usando uma sessão.
- [`SessionParams.py`](./SessionParams.py): Aplica parâmetros padrão às requisições da sessão.

## Autenticação e cookies

- [`AuthBasic.py`](./AuthBasic.py): Faz autenticação HTTP Basic.
- [`AuthCustom.py`](./AuthCustom.py): Acrescenta um cabeçalho com autenticação personalizada.
- [`AuthDigest.py`](./AuthDigest.py): Faz autenticação HTTP Digest.
- [`AuthProxy.py`](./AuthProxy.py): Cria objeto de autenticação para proxy.
- [`CookieAddDict.py`](./CookieAddDict.py): Adiciona um dicionário de cookies ao CookieJar.
- [`CookieDictFromJar.py`](./CookieDictFromJar.py): Converte CookieJar em dicionário.
- [`CookieJarFromDict.py`](./CookieJarFromDict.py): Cria CookieJar a partir de um dicionário.

## Utilidades e erros

- [`HttpCodes.py`](./HttpCodes.py): Consulta códigos HTTP pelos nomes conhecidos.
- [`RequestsExceptions.py`](./RequestsExceptions.py): Trata timeout, conexão, status e JSON inválido.
- [`UtilsEncodings.py`](./UtilsEncodings.py): Encontra codificações declaradas no HTML.
- [`UtilsHeaderEncoding.py`](./UtilsHeaderEncoding.py): Obtém codificação a partir dos cabeçalhos.
- [`UtilsUnicode.py`](./UtilsUnicode.py): Obtém o conteúdo de resposta como texto Unicode.

## Arquivos, hooks e adaptadores

- [`DownloadFile.py`](./DownloadFile.py): Baixa um arquivo e salva no diretório atual.
- [`DownloadStream.py`](./DownloadStream.py): Baixa um arquivo em blocos para poupar memória.
- [`HttpAdapter.py`](./HttpAdapter.py): Configura adaptador, pool e tentativas da sessão.
- [`ResponseHook.py`](./ResponseHook.py): Executa uma função assim que a resposta chega.
- [`UploadFile.py`](./UploadFile.py): Envia documento.txt como arquivo multipart.
