<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/project_etl_heroby on 2026-07-31 -->

## Consulta dos dados da plataforma
----
Esse app automatiza o download de todos os dados armazenados na plataforma Heroby utilizando a LIB BOTO3 para acessar os serviços DynamoDB.
----
## Passo-passo
Antes de tudo, instale os seguintes arquivos e configure-os corretamente:
  - GIT: [REDACTED_URL]
  - Python 3; [REDACTED_URL]
  - AWS-CLI: [REDACTED_URL]
    - Digite AWS CONFIGURE e insira as credenciais do desenvolvedor.

1. Clonar o repositório
2. No terminal, entre dentro da pasta do projeto e crie um ambiente virtual digitando: python3 -m venv .env
3. Ative o ambiente virtual de acordo com seu O.S
4. Instale as bibliotecas necessárias para rodar esse projeto digitando: pip3 install -r requirements.txt
- Boto3
- Pandas
- xlsxwriter

Depois sempre inicie o programa digitando: python3 consulta.py
---

<br>
[1] Extrair todos os dispositivos - Em desenvolvimento<br>
[2] Extrair dados de Beacons;<br>
[3] Extrair dados de Gateways;<br>
[4] Sair do sistema.