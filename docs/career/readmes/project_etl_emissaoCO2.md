<!-- synced from https://github.com/devzurc/project_etl_emissaoCO2 on 2026-06-12 -->

<!-- career curation note: treat this as a personal learning/lab repo. Scenario language below about a company/team is not verified employer or client evidence; no production deployment, ownership claim, business metric, or client outcome is verified from this README. -->

# ETL Pipeline - Análise de Emissões de CO2

## Sobre o Projeto
Este projeto foi desenvolvido para processar e analisar os dados do conjunto "Emissão_CO2_por_países.csv". A pipeline ETL segue a arquitetura Medallion (Bronze, Silver, Gold) para garantir eficiência no armazenamento e processamento dos dados, facilitando análises avançadas para a equipe de sustentabilidade e gestão de carbono da empresa.

## Objetivos da Missão
1. **Transformação dos dados:** Converter os dados para o formato Parquet para otimizar armazenamento e processamento.
2. **Leitura dos arquivos:** Demonstrar como carregar e processar arquivos Parquet.
3. **Análise inicial:** Apresentar a soma de "Kilotons of Co2" por "Region".
4. **Desafio Extra:** Explorar padrões nos dados e identificar regiões com potencial para redução de emissões.

## Arquitetura do Pipeline
```text
📂 data-lakehouse/
 ├── 📂 bronze/  # Armazena os dados brutos em Parquet
 ├── 📂 silver/  # Dados processados e limpos
 ├── 📂 gold/    # Dados prontos para análise de BI
 ├── 📂 logs/    # Arquivos de log do pipeline
```

## Tecnologias Utilizadas
- **Python** (ETL e análise de dados)
- **Pandas** (Manipulação e limpeza de dados)
- **PyArrow** (Conversão e processamento Parquet)
- **Logging** (Monitoramento do pipeline)

## Configuração do Projeto

### Pré-requisitos
- Python 3.x instalado

## Como Executar o Pipeline Usando o `start.sh`
### 1️⃣ Dando Permissão ao Script `start.sh`

No terminal, navegue até o diretório onde o arquivo `start.sh` está localizado. Suponhamos que o arquivo esteja na pasta **Downloads**:
```sh
cd ~/Downloads
```

Em seguida, torne o script executável com o comando:
```sh
chmod +x start.sh
```

### 2️⃣ Executando o Script `start.sh`

Agora, para rodar o script, execute o seguinte comando no terminal:
```sh
./start.sh
```
Ou, caso necessário, execute usando o Bash:
```sh
bash start.sh
```

### 3️⃣ O Que o Script `start.sh` Faz

O script `start.sh` realiza os seguintes passos automaticamente:
1. **Criação do ambiente virtual (.venv):** Cria e ativa o ambiente virtual para garantir que todas as dependências necessárias sejam isoladas.
2. **Instalação das dependências:** Instala todas as dependências listadas no arquivo `requirements.txt`.
3. **Execução do ETL:** Roda o pipeline ETL, que realiza as transformações e gera os dados processados nas camadas Bronze, Silver e Gold.
4. **Execução do Jupyter Notebook:** Após a execução do ETL, abre o Jupyter Notebook **`analysis.ipynb`** para que você possa visualizar e interagir com os dashboards atualizados.

## Explicação das Camadas

### 🟤 Bronze Layer
- Converte o CSV em Parquet e salva na camada Bronze sem modificar os dados.

### ⚪ Silver Layer
- Processa e limpa os dados:
  - Faz a limpeza e padronizacao dos dados.
  - Ajusta tipos de dados.
  - Renomeia colunas para um padrão consistente.

### 🟡 Gold Layer
- Gera insights para Business Intelligence, como:
  - Total de CO2 emitido por região.
  - Países com maior emissão de CO2.
  - Regiões com maior potencial de redução de emissões.

## 📜 Logs e Monitoramento
Os logs do pipeline são salvos no diretório `logs/etl_pipeline.log`.
