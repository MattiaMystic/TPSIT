import socket

def prendi_input():
    numero = input("Numero di biglietti: ")

    if not numero.isdigit() or int(numero) <= 0:
        print("Errore: numero non valido")
        return None

    return numero


def mostra_risultato(risposta):
    if risposta == "ERRORE":
        print("Errore nei dati inseriti")
    else:
        vincenti, premio, costo, guadagno = risposta.split(",")

        print("Biglietti vincenti:", vincenti)
        print("Premio totale:", premio, "€")
        print("Costo totale:", costo, "€")
        print("Guadagno:", guadagno, "€")


def start_client():
    numero = prendi_input()

    if numero is None:
        return

    client = socket.socket()
    client.connect(("localhost", 12345))

    client.send(numero.encode())

    risposta = client.recv(1024).decode()

    client.close()

    mostra_risultato(risposta)


if __name__ == "__main__":
    start_client()
