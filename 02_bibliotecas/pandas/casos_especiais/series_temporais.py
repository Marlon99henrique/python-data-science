"""
📊 Séries Temporais com Pandas

Este script demonstra manipulação de dados temporais no Pandas:
- Criação e indexação por datas
- Filtros temporais
- Reamostragem (resample)
- Janelas móveis (rolling)
- Estatísticas sobre séries temporais
"""

import pandas as pd
import numpy as np

# =========================
# 1. Criação de Série Temporal
# =========================

# Criando um intervalo de datas (diário)
datas = pd.date_range(start="2024-01-01", periods=100, freq="D")

# Simulando série temporal (valores de vendas)
np.random.seed(42)
vendas = np.random.randint(50, 200, size=100)

serie_vendas = pd.Series(vendas, index=datas)
print("📌 Série Temporal (primeiras linhas):")
print(serie_vendas.head())


# =========================
# 2. Seleção por Datas
# =========================

print("\n📌 Vendas em Janeiro de 2024:")
print(serie_vendas["2024-01"])

print("\n📌 Vendas em um intervalo específico:")
print(serie_vendas["2024-02-10":"2024-02-20"])


# =========================
# 3. Reamostragem
# =========================

# Média semanal
media_semanal = serie_vendas.resample("W").mean()
print("\n📌 Média Semanal:")
print(media_semanal.head())

# Soma mensal
soma_mensal = serie_vendas.resample("M").sum()
print("\n📌 Soma Mensal:")
print(soma_mensal)


# =========================
# 4. Janelas Móveis
# =========================

# Média móvel de 7 dias
media_movel = serie_vendas.rolling(window=7).mean()
print("\n📌 Média Móvel (7 dias):")
print(media_movel.head(15))


# =========================
# 5. Estatísticas
# =========================

print("\n📌 Estatísticas gerais da série temporal:")
print(serie_vendas.describe())

print("\n📌 Dia com maior venda:")
print(serie_vendas.idxmax(), "→", serie_vendas.max())

print("\n📌 Dia com menor venda:")
print(serie_vendas.idxmin(), "→", serie_vendas.min())
