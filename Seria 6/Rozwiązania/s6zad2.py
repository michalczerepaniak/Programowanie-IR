macierz = [
    [4, 7, 1],
    [9, 2, 6],
    [3, 8, 5]
]

pozycje = []
suma = 0

for i, wiersz in enumerate(macierz):
    for j, wartosc in enumerate(wiersz):
        if wartosc > 5:
            pozycje.append((i, j))
            suma += wartosc