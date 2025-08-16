"""
📂 Tratamento de Arquivos em Python - Fundamentos para Ciência de Dados

Este script demonstra:
1. Leitura/escrita de arquivos .txt, .csv e .json
2. Bibliotecas padrão (open) e Pandas (para dados estruturados)
3. Tratamento de exceções e encoding

Métodos aplicáveis em:
- Importação/exportação de datasets
- Limpeza de dados brutos
- Integração com APIs (JSON)
"""

# Importa o módulo csv para manipulação de arquivos CSV
import csv

# Importa o módulo json para leitura e escrita de arquivos JSON
import json

# Importa o pandas, biblioteca poderosa para análise de dados
import pandas as pd

# Importa Path da biblioteca pathlib para manipulação de caminhos de arquivos
from pathlib import Path


# ==================== 1. MANIPULAÇÃO BÁSICA (TXT) ====================
def exemplo_txt():
    """Lê e escreve em arquivos texto (logs, dados não-tabulados)."""
    try:
        # Abre (ou cria) o arquivo 'dados.txt' para escrita, usando codificação UTF-8
        with open("dados.txt", "w", encoding="utf-8") as f:
            f.write("Data: 2023-10-01\n")  # Escreve uma linha com data
            f.write("Produto: Notebook, Quantidade: 5\n")  # Escreve dados do produto

        # Abre o mesmo arquivo para leitura
        with open("dados.txt", "r", encoding="utf-8") as f:
            print("\nConteúdo do arquivo TXT:")
            for linha in f:  # Itera sobre cada linha do arquivo
                print(linha.strip())  # Imprime a linha sem quebras de linha

    # Captura erro caso o arquivo não seja encontrado
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado!")

    # Captura erro de codificação (ex: UTF-8 mal formatado)
    except UnicodeDecodeError:
        print("Erro: Encoding inválido (use utf-8).")

# ==================== 2. TRABALHANDO COM CSV ====================
def exemplo_csv():
    """Processa arquivos CSV (com módulo csv e pandas)."""
    # Criando um CSV manualmente
    cabecalho = ["id", "nome", "preco"]
    dados = [
        [1, "Mouse", 89.90],
        [2, "Teclado", 199.90],
    ]

    with open("produtos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(cabecalho)
        writer.writerows(dados)

    # Lendo com Pandas (mais comum em DS)
    df = pd.read_csv("produtos.csv", delimiter=";")
    print("\nDataFrame do CSV:")
    print(df.head())

# ==================== 3. PROCESSANDO JSON ====================
def exemplo_json():
    """Lê e escreve JSON (comum em APIs e configurações)."""
    dados_api = {
        "cliente": {
            "id": 123,
            "nome": "Ana Silva",
            "compras": [{"produto": "Monitor", "valor": 799.90}]
        }
    }

    # Salvando
    with open("cliente.json", "w", encoding="utf-8") as f:
        json.dump(dados_api, f, indent=4)  # indent formata o JSON

    # Lendo
    with open("cliente.json", "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)
        print("\nDados do JSON:")
        print(f"Nome do cliente: {dados_lidos['cliente']['nome']}")

# ==================== 4. BOAS PRÁTICAS ====================
def verifica_arquivos():
    """Checa se arquivos existem antes de processar (evita erros)."""
    arquivos = ["dados.txt", "produtos.csv", "cliente.json"]
    for arquivo in arquivos:
        path = Path(arquivo)
        if path.exists():
            print(f"\n✅ {arquivo} encontrado ({path.stat().st_size} bytes)")
        else:
            print(f"\n❌ {arquivo} não existe!")

# ==================== EXECUÇÃO ====================
if __name__ == "__main__":
    exemplo_txt()
    exemplo_csv()
    exemplo_json()
    verifica_arquivos()