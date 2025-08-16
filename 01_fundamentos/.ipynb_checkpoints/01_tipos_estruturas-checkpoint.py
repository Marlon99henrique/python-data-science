"""
📌 Tipos de Dados e Estruturas em Python - Fundamentos para Ciência de Dados

Este script cobre:
1. Tipos primitivos (int, float, str, bool)
2. Estruturas de dados (listas, tuplas, dicionários, sets)
3. Operações essenciais para análise e transformação de dados
"""

# ==================== 1. TIPOS PRIMITIVOS ====================
# Inteiros e floats — usados em cálculos estatísticos
idade = 25
preco_medio = 19.99

# Strings — úteis na manipulação de texto em dados categóricos
nome_produto = "Notebook Gamer"

# Booleanos — aplicados em filtros e condições
ativo = True

# ==================== 2. LISTAS ====================
# Sequências ordenadas — representam colunas ou séries de dados
vendas = [120, 89, 150, 42]

# Operações comuns
media_vendas = sum(vendas) / len(vendas)
vendas.append(200)
vendas.extend([30, 70])

# List comprehension — transformação condicional
vendas_dobro = [v * 2 for v in vendas if v > 50]

# ==================== 3. TUPLAS ====================
# Estruturas imutáveis — úteis para registros fixos
coordenadas = (-23.5489, -46.6388)

# ==================== 4. DICIONÁRIOS ====================
# Pares chave-valor — muito usados em JSON e metadados
produto = {
    "id": 123,
    "nome": "Teclado Mecânico",
    "estoque": 45,
    "disponivel": True
}

# Acesso seguro com .get()
qtd_estoque = produto.get("estoque", 0)

# ==================== 5. SETS ====================
# Coleções únicas — úteis para eliminar duplicatas
categorias = {"eletrônicos", "informática", "eletrônicos"}

# ==================== 6. APLICAÇÃO EM CIÊNCIA DE DADOS ====================
# Exemplo: contagem de itens únicos em uma coluna simulada
dados_brutos = ["SP", "RJ", "MG", "SP", "RJ"]
estados_unicos = set(dados_brutos)

# Conversão entre estruturas — comum em pipelines
lista_para_dict = {k: v for k, v in enumerate(vendas)}

# ==================== EXECUÇÃO ====================
if __name__ == "__main__":
    print(f" Produto: {nome_produto.upper()}")
    print(f" Média de vendas: {media_vendas:.2f}")
    print(f" Latitude: {coordenadas[0]}")
    print(f" Estoque disponível: {qtd_estoque}")
    print(f" Categorias únicas: {categorias}")
    print(f" Estados únicos: {estados_unicos}")
    print(f" Lista convertida em dicionário: {lista_para_dict}")