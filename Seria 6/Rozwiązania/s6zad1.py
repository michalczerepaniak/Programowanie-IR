slowa = ["kot", "samochod", "drzewo", "dom", "informatyka"]

indeksy = []
suma_znakow = 0

for i, slowo in enumerate(slowa):
    if len(slowo) > 4:
        indeksy.append(i)
        suma_znakow += len(slowo)