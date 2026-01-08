def valore_totale(prodotti):
    totale = 0
    for p in prodotti:
        totale += p["prezzo"] * p["quantità"]
    return totale


prodotti = []

menu = """
MENU MAGAZZINO
1 - Aggiungi prodotto
2 - Valore totale magazzino
3 - Prodotto con valore più alto
4 - Prodotti esauriti
0 - Esci
"""

while True:
    scelta = input(menu)

    if scelta == "1":
        nome = input("Nome prodotto: ")
        prezzo = float(input("Prezzo: "))
        quantità = int(input("Quantità: "))

        prodotti.append({
            "nome": nome,
            "prezzo": prezzo,
            "quantità": quantità
        })

        print("Prodotto aggiunto")

    elif scelta == "2":
        print("Valore totale:", valore_totale(prodotti))

    elif scelta == "3":
        max_valore = 0
        nome_max = ""

        for p in prodotti:
            valore = p["prezzo"] * p["quantità"]
            if valore > max_valore:
                max_valore = valore
                nome_max = p["nome"]

        print("Prodotto più prezioso:", nome_max)

    elif scelta == "4":
        esauriti = []

        for p in prodotti:
            if p["quantità"] == 0:
                esauriti.append(p["nome"])

        print("Prodotti esauriti:", esauriti)

    elif scelta == "0":
        print("Uscita")
        break

    else:
        print("Opzione non valida")
