import numpy as np

macierz = np.array([
    [4, 7, 1],
    [9, 2, 6],
    [3, 8, 5]
])

# Elementy > 5
maska = macierz > 5

# Indeksy
indeksy = np.argwhere(maska)

# Suma
suma = np.sum(macierz[maska])