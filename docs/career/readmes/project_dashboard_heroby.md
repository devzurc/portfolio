<!-- synced from https://github.com/devzurc/project_dashboard_heroby on 2026-06-17 -->

# Auto Dashboard HeroBy
## RPA ETL passando os dados para Dashboards em Excel e enviados automáticamente para os clientes.

I'm a Data Science enthusiast trying to learn everything I think I need to become a better Data Scientist.



Antes de tudo, instale os seguintes arquivos e configure-os corretamente:
  - GIT: https://git-scm.com/downloads
  - Python 3; https://www.python.org/downloads/
  - AWS-CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
    - Digite AWS CONFIGURE e insira as credenciais do desenvolvedor.
Nesse projeto, utilizamos as seguintes LIBS:
Dentro da pasta do projeto, voce consegue instalar as seguintes libs digitando o comando: pip install -r requiriments.txt
  - Boto3
  - Psycopg2-binary
  - Openpyxl
  - Pandas
  - Pytest-shutil
  - Python-dotenv
  - xlsxwriter
 ________________________________________________________________________________________________________________________________________________________
# Iniciando o sistema
## EXTRAIR DADOS PARA O DASHBOARD:
1. Abra o arquivo main.py
2. Selecione a opção 1 (extrair dados do database):
3. Environment: “prod” <br>
  a. Data inicial exemplo: ``13/12/2021`` <br>
  b. Data final exemplo: ``18/12/2021 ``
4. Aguarde o menu aparecer novamente e NÃO FECHE O TERMINAL

## TRANSFERIR DADOS EXTRAÍDOS PARA O ARQUIVO DASHBOARD:
1. Entre na pasta “reports”
2. Pasta “dashboard”: Cópias do arquivo “dash_heroby.xlsx” nomeadas para cada empresa e com a data do período selecionado na extração dos dados.
3. Pasta “data”: arquivos excel com dados de incidentes, beacon e gateway de cada cliente que gerou evento durante o período selecionado.
4. Pasta “devices”: arquivos com dados de beacon e gateway de cada cliente que não gerou eventos durante o período selecionado.
5. Iniciaremos a transferência de dados dos arquivos da pasta “data” para os arquivos da pasta “dashboard”
  a. Abra o arquivo da empresa em “data” e cole no arquivo da mesma empresa na pasta “dashboard”.
  b. Após a transferência de dados, selecione toda a coluna de horário.
  c. Com a coluna selecionada, escolha a ferramenta “texto para colunas” e clique em concluir.
6. Oculte a sheet “events” para esconder a tabela.
7. Atualize todas as tabelas dinâmicas e gráficos do arquivo.
8. Confira os dados com a plataforma web de cada empresa.


## ENVIAR OS DASHBOARDS VIA E-MAIL PARA OS CLIENTES:
1. Abra o terminal onde está o menu do auto dashboard
2. Escolha a opção de 3: enviar e-mail
3. Faremos um teste escolhendo a opção 1, insira o e-mail onde deseja receber os dashboards;
4. Confira se recebeu todos os e-mails corretamente e se os números condizem com a plataforma;
5. Após realizar o teste, envie os dashboards para os clientes escolhendo a opção 2.