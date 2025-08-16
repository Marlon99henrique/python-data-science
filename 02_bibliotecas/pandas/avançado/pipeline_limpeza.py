"""
pipeline_limpeza.py

Exemplo de pipeline de pré-processamento de dados para projetos de Ciência de Dados.
Mostra boas práticas de limpeza, transformação e preparação de datasets reais.

Este arquivo mostra:
- Estrutura de pipeline profissional
- Boas práticas de funções reutilizáveis
- Tratamento de missing, normalização e codificação
- Código pronto para projetos e portfólio

Autor: Marlon Henrique
"""

import pandas as pd
import numpy as np

# ===============================
# 1. Carregamento de Dados
# ===============================
def carregar_dados(caminho_csv):
    """
    Carrega dados de um arquivo CSV para um DataFrame.

    Args:
        caminho_csv (str): Caminho do arquivo CSV.
    
    Returns:
        pd.DataFrame: DataFrame com os dados carregados.
    """
    df = pd.read_csv(caminho_csv)
    return df

# ===============================
# 2. Tratamento de Valores Ausentes
# ===============================
def tratar_missing(df):
    """
    Realiza tratamento de valores ausentes.

    Estratégias:
        - Colunas numéricas: preencher com mediana
        - Colunas categóricas: preencher com modo

    Args:
        df (pd.DataFrame): DataFrame original.
    
    Returns:
        pd.DataFrame: DataFrame sem valores ausentes.
    """
    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)
    return df

# ===============================
# 3. Normalização de Dados Numéricos
# ===============================
def normalizar_numericos(df, colunas):
    """
    Normaliza colunas numéricas usando Min-Max Scaling.

    Args:
        df (pd.DataFrame): DataFrame original.
        colunas (list): Lista de colunas numéricas.
    
    Returns:
        pd.DataFrame: DataFrame com colunas normalizadas.
    """
    for col in colunas:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)
    return df

# ===============================
# 4. Codificação de Variáveis Categóricas
# ===============================
def codificar_categoricas(df, colunas):
    """
    Realiza codificação de colunas categóricas usando Label Encoding.

    Args:
        df (pd.DataFrame): DataFrame original.
        colunas (list): Lista de colunas categóricas.
    
    Returns:
        pd.DataFrame: DataFrame com colunas codificadas.
    """
    for col in colunas:
        df[col] = df[col].astype("category").cat.codes
    return df

# ===============================
# 5. Pipeline Completo
# ===============================
def pipeline_completo(caminho_csv, colunas_numericas, colunas_categoricas):
    """
    Executa todo o pipeline de pré-processamento de dados.

    Args:
        caminho_csv (str): Caminho do arquivo CSV.
        colunas_numericas (list): Lista de colunas numéricas para normalizar.
        colunas_categoricas (list): Lista de colunas categóricas para codificar.
    
    Returns:
        pd.DataFrame: DataFrame pronto para análise ou modelagem.
    """
    df = carregar_dados(caminho_csv)
    df = tratar_missing(df)
    df = normalizar_numericos(df, colunas_numericas)
    df = codificar_categoricas(df, colunas_categoricas)
    return df

# ===============================
# Exemplo de uso
# ===============================
if __name__ == "__main__":
    df_final = pipeline_completo(
        "dados/exemplo.csv",
        colunas_numericas=["idade", "salario"],
        colunas_categoricas=["sexo", "departamento"]
    )
    print(df_final.head())
