frase = ""
parole = []

menu = """
MENU ANALISI FRASE
1 - Inserisci frase
2 - Lista parole
3 - Conteggio parole
4 - Parola più lunga e più corta
5 - Parole ripetute
0 - Esci
"""

while True:
    scelta = input(menu)

    if scelta == "1":
        frase = input("Inserisci una frase: ")
        parole = frase.split()#split divide la stringa in base agli spazi e crea una lista di parole
        print("Frase inserita")

    elif scelta == "2":
        print("Parole:", parole)

    elif scelta == "3":
        conteggio = len(parole)

        print("Conteggio:", conteggio)

    elif scelta == "4":
        lunga = parole[0]
        corta = parole[0]

        for p in parole:
            if len(p) > len(lunga):
                lunga = p
            if len(p) < len(corta):
                corta = p

        print("Più lunga:", lunga)
        print("Più corta:", corta)

    elif scelta == "5":
        ripetute = []
        for p in parole:
            if parole.count(p) > 1 and p not in ripetute:
                ripetute.append(p)

        print("Parole ripetute:", ripetute)

    elif scelta == "0":
        print("Uscita")
        break

    else:
        print("Opzione non valida")
