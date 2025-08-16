"""
🔢 Operações Básicas com NumPy

Este script demonstra as operações fundamentais em arrays NumPy:
- Operações aritméticas
- Funções estatísticas
- Funções matemáticas
- Broadcasting
"""

import numpy as np

# ---------------------------
# Criando arrays de exemplo
# ---------------------------
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("Array a:", a)
print("Array b:", b)

# ---------------------------
# Operações aritméticas
# ---------------------------
print("\n--- Operações Aritméticas ---")
print("Soma:", a + b)
print("Subtração:", b - a)
print("Multiplicação:", a * b)
print("Divisão:", b / a)
print("Potenciação:", a ** 2)

# ---------------------------
# Funções estatísticas
# ---------------------------
print("\n--- Estatísticas ---")
print("Soma dos elementos:", a.sum())
print("Média:", a.mean())
print("Mínimo:", a.min())
print("Máximo:", a.max())
print("Desvio Padrão:", a.std())

# ---------------------------
# Funções matemáticas
# ---------------------------
print("\n--- Funções Matemáticas ---")
c = np.array([0, np.pi/2, np.pi])
print("Seno:", np.sin(c))
print("Cosseno:", np.cos(c))
print("Exponencial:", np.exp(a))
print("Logaritmo:", np.log(a))

# ---------------------------
# Broadcasting
# ---------------------------
print("\n--- Broadcasting ---")
matriz = np.ones((3, 3)) * 5
print("Matriz base:\n", matriz)

# Operação com escalar
print("Matriz + 2:\n", matriz + 2)

# Operação entre array 1D e 2D
vetor = np.array([1, 2, 3])
print("Matriz + vetor:\n", matriz + vetor)
