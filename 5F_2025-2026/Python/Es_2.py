def calcola_media(voti):
    return sum(voti) / len(voti)


studenti = []  #lista di studenti

menu = """
MENU OPZIONI
1 - Aggiungi studente
2 - Visualizza riepilogo studenti
3 - Studente con media più alta
4 - Studente con media più bassa
5 - Elenco studenti promossi
0 - Esci
"""

while True:
    scelta = input(menu)



    # 1) Inserimento studente
    if scelta == "1":
        nome = input("Nome studente: ")
        voti = input("Inserisci i voti separati da spazio: ")
        voti = list(map(int, voti.split()))#map applica int a ogni elemento della lista ottenuta da split che divide la stringa in base agli spazi

        studenti.append({
            "nome": nome,
            "voti": voti
        })

        print("Studente inserito correttamente")

    # 2) Riepilogo studenti
    elif scelta == "2":
        print("\nRIEPILOGO STUDENTI")
        for s in studenti:
            media = calcola_media(s["voti"])
            stato = "Promosso" if media >= 6 else "Bocciato"
            print(s["nome"], "- Media:", media, ":", stato)

    # 3) Studente con media più alta
    elif scelta == "3":
        media_max = -1
        nome_max = ""

        for s in studenti:
            media = calcola_media(s["voti"])
            if media > media_max:
                media_max = media
                nome_max = s["nome"]

        print("Studente con media più alta:", nome_max, ":", media_max)

    # 4) Studente con media più bassa
    elif scelta == "4":
        media_min = 11
        nome_min = ""

        for s in studenti:
            media = calcola_media(s["voti"])
            if media < media_min:
                media_min = media
                nome_min = s["nome"]

        print("Studente con media più bassa:", nome_min, ":", media_min)

    # 5) Elenco studenti promossi
    elif scelta == "5":
        promossi = []

        for s in studenti:
            if calcola_media(s["voti"]) >= 6:
                promossi.append(s["nome"])

        print("Studenti promossi:", promossi)

    # 0) Uscita
    elif scelta == "0":
        print("Uscita dal programma")
        break

    # Scelta non valida
    else:
        print("Opzione non valida, riprova")
