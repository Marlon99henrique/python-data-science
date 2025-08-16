"""
MANIPULAÇÃO DE MEMÓRIA EM NUMPY
---------------------------------
Este script demonstra:
1. Views vs Cópias
2. Alocação eficiente de arrays
3. Gerenciamento de memória
4. Otimizações para grandes datasets
"""

import numpy as np
import sys
import time
import gc  # Movido para o topo do arquivo

def main():
    print("=== 1. Views vs Cópias ===")
    # Criando um array original
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array original: {arr}")

    # Criando uma view (não aloca nova memória)
    arr_view = arr[:3]
    print(f"View das 3 primeiras posições: {arr_view}")

    # Modificando a view (altera o original)
    arr_view[0] = 100
    print(f"Array após modificar view: {arr}")

    # Criando uma cópia (aloca nova memória)
    arr_copy = arr.copy()
    arr_copy[0] = 999
    print(f"Cópia modificada: {arr_copy}")
    print(f"Array original permanece inalterado: {arr}")

    print("\n=== 2. Alocação Eficiente ===")
    # Pré-alocação de memória
    size = 1_000_000
    print(f"Alocando array com {size:,} elementos...")

    # Maneira ineficiente (crescendo dinamicamente)
    start = time.time()
    slow_arr = np.array([])
    for i in range(size):
        slow_arr = np.append(slow_arr, i)
    print(f"Maneira lenta: {time.time() - start:.2f} segundos")

    # Maneira eficiente (pré-alocação)
    start = time.time()
    fast_arr = np.empty(size)
    for i in range(size):
        fast_arr[i] = i
    print(f"Maneira rápida: {time.time() - start:.2f} segundos")

    print("\n=== 3. Gerenciamento de Memória ===")
    # Verificando uso de memória
    big_array = np.ones((1000, 1000))
    print(f"Tamanho do array 1000x1000: {big_array.nbytes / 1e6:.2f} MB")

    # Liberando memória explicitamente
    del big_array
    gc.collect()
    print("Memória liberada")

    print("\n=== 4. Otimizações para Grandes Datasets ===")
    # Usando memmap para arrays maiores que a RAM
    filename = 'large_array.dat'
    shape = (5000, 5000)
    dtype = np.float32

    # Cria array mapeado em disco
    mmap_arr = np.memmap(filename, dtype=dtype, mode='w+', shape=shape)
    mmap_arr[:] = np.random.rand(*shape)
    print(f"Array de {shape} salvo em disco: {filename}")
    print(f"Uso de memória RAM: {sys.getsizeof(mmap_arr) / 1e6:.2f} MB")

    # Fechando o memmap
    del mmap_arr

if __name__ == "__main__":
    main()