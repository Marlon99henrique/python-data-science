"""
📌 Tipos de Dados e Estruturas em Python - Fundamentos para Ciência de Dados

Este script cobre:
1. Tipos primitivos (int, float, str, bool)
2. Estruturas de dados (listas, tuplas, dicionários, sets)
3. Operações essenciais para análise de dados
"""

# ==================== 1. TIPOS PRIMITIVOS ====================
# Inteiros e floats (usados em cálculos estatísticos)
idade = 25
preco_medio = 19.99

# Strings (manipulação de texto em dados categóricos)
nome_produto = "Notebook Gamer"
print(f"Produto: {nome_produto.upper()}")  # Métodos úteis

# Booleanos (filtros em DataFrames)
ativo = True

# ==================== 2. LISTAS ====================
# Usadas para sequências ordenadas (ex: colunas de datasets)
vendas = [120, 89, 150, 42]
print(f"\nMédia de vendas: {sum(vendas)/len(vendas):.2f}")

# Métodos úteis:
vendas.append(200)  # Adiciona item
vendas.extend([30, 70])  # Adiciona múltiplos itens

# List Comprehension (importante para transformações)
vendas_dobro = [v * 2 for v in vendas if v > 50]

# ==================== 3. TUPLAS ====================
# Imutáveis (ex: coordenadas, registros fixos)
coordenadas = (-23.5489, -46.6388)
print(f"\nLatitude: {coordenadas[0]}")

# ==================== 4. DICIONÁRIOS ====================
# Pares chave-valor (ex: dados JSON, metadados)
produto = {
    "id": 123,
    "nome": "Teclado Mecânico",
    "estoque": 45,
    "disponivel": True
}

# Acesso seguro (evita KeyError)
qtd_estoque = produto.get("estoque", 0)

# ==================== 5. SETS ====================
# Coleções não-ordenadas e únicas (ex: remoção de duplicatas)
categorias = {"eletrônicos", "informática", "eletrônicos"}
print(f"\nCategorias únicas: {categorias}")

# ==================== 6. APLICAÇÃO EM CIÊNCIA DE DADOS ====================
# Exemplo: Contagem de itens únicos em uma coluna (simulação)
dados_brutos = ["SP", "RJ", "MG", "SP", "RJ"]
estados_unicos = set(dados_brutos)  # Remove duplicatas
print(f"\nEstados únicos: {estados_unicos}")

# Conversão entre estruturas (comum em pipelines)
lista_para_dict = {k: v for k, v in enumerate(vendas)}