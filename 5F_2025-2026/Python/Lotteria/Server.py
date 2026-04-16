import socket
import random

def calcola_lotteria(num_biglietti):
    prezzo = 2
    probabilita = 10
    premio = 20

    vincenti = 0

    for i in range(num_biglietti):
        if random.randint(1, probabilita) == 1:
            vincenti += 1

    costo = num_biglietti * prezzo
    premio_tot = vincenti * premio
    guadagno = premio_tot - costo

    return f"{vincenti},{premio_tot},{costo},{guadagno}"


def start_server():
    server = socket.socket()
    server.bind(("localhost", 12345))
    server.listen(1)

    print("Server in ascolto...")

    conn, addr = server.accept()

    dati = conn.recv(1024).decode()

    try:
        num_biglietti = int(dati)

        if num_biglietti <= 0:
            risultato = "ERRORE"
        else:
            risultato = calcola_lotteria(num_biglietti)

    except:
        risultato = "ERRORE"

    conn.send(risultato.encode())

    conn.close()
    server.close()


if __name__ == "__main__":
    start_server()
