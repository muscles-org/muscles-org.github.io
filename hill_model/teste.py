import numpy as np

# Array L inicial
L = np.full(250, 1.0)
print(L)

# Array a ser adicionado
array_a_adicionar = np.arange(1, 0.5, -0.01)

print(array_a_adicionar)

print(L+array_a_adicionar[:, np.newaxis])

# # Repetir o array a ser adicionado para ter o mesmo tamanho que L
# array_repetido = np.tile(array_a_adicionar, len(L) // len(array_a_adicionar) + 1)

# # Adicionar o array a cada elemento de L
# L += array_repetido[:len(L)]

# print(L)