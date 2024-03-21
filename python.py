import time
import numpy as np

# Gerando um vetor de inteiros aleatórios
N = 10000
vetor = np.random.randint(0, high=100, size=N, dtype=int)

# Medindo o tempo de processamento
start = time.time()

# Algoritmo de ordenação Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

vetor_ordenado = bubble_sort(vetor)

end = time.time()

print(f'Tempo decorrido: {end-start}')
