def calcola_media(lista):
    return sum(lista) / len(lista)


numeri = []

menu = """
MENU STATISTICHE
1 - Inserisci numeri
2 - Calcola media
3 - Numeri sopra e sotto la media
4 - Numeri maggiori della media
5 - Sequenza più lunga di numeri uguali
0 - Esci
"""

while True:
    scelta = input(menu)

    if scelta == "1":
        numeri = list(map(int, input("Inserisci numeri separati da spazio: ").split()))
        print("Numeri inseriti")

    elif scelta == "2":
        print("Media:", calcola_media(numeri))

    elif scelta == "3":
        m = calcola_media(numeri)
        sopra = 0
        sotto = 0

        for n in numeri:
            if n > m:
                sopra += 1
            elif n < m:
                sotto += 1

        print("Sopra la media:", sopra)
        print("Sotto la media:", sotto)

    elif scelta == "4":
        m = calcola_media(numeri)
        maggiori = []

        for n in numeri:
            if n > m:
                maggiori.append(n)

        print("Numeri maggiori della media:", maggiori)

    elif scelta == "5":
        max_seq = 1
        seq = 1

        for i in range(1, len(numeri)):
            if numeri[i] == numeri[i - 1]:
                seq += 1
                if seq > max_seq:
                    max_seq = seq
            else:
                seq = 1

        print("Sequenza più lunga:", max_seq)

    elif scelta == "0":
        print("Uscita")
        break

    else:
        print("Opzione non valida")
