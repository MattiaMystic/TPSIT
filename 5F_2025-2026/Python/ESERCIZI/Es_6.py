def saldo_finale(operazioni):
    return sum(operazioni)


operazioni = []

menu = """
MENU CONTO BANCARIO
1 - Inserisci operazioni
2 - Saldo finale
3 - Saldo massimo e minimo
4 - Numero depositi e prelievi
5 - Saldi dopo ogni operazione
0 - Esci
"""

while True:
    scelta = input(menu)

    if scelta == "1":
        operazioni = list(map(int, input("Inserisci operazioni: ").split()))

    elif scelta == "2":
        print("Saldo finale:", saldo_finale(operazioni))

    elif scelta == "3":
        saldo = 0
        max_saldo = 0
        min_saldo = 0

        for op in operazioni:
            saldo += op
            if saldo > max_saldo:
                max_saldo = saldo
            if saldo < min_saldo:
                min_saldo = saldo

        print("Saldo massimo:", max_saldo)
        print("Saldo minimo:", min_saldo)

    elif scelta == "4":
        depositi = 0
        prelievi = 0

        for op in operazioni:
            if op > 0:
                depositi += 1
            else:
                prelievi += 1

        print("Depositi:", depositi)
        print("Prelievi:", prelievi)

    elif scelta == "5":
        saldo = 0
        saldi = []

        for op in operazioni:
            saldo += op
            saldi.append(saldo)

        print("Saldi:", saldi)

    elif scelta == "0":
        print("Uscita")
        break

    else:
        print("Opzione non valida")
