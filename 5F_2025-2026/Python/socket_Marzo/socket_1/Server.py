import socket
import threading

def gestisci_client(conn, addr):
    print(f"Connesso con {addr}")
    try:
        # Riceviamo i dati (es: "id_ristorante;importo;distanza")
        data = conn.recv(1024).decode('utf-8')
        if not data:
            return

        # Dividiamo la stringa usando il separatore ';'
        parti = data.split(';')
        rist_id = parti[0]
        importo = float(parti[1])
        distanza = float(parti[2])

        # Dati ristoranti
        ristoranti = {
            "1": {"nome": "Pizzeria", "fisso": 2.5, "km": 0.5},
            "2": {"nome": "Sushi", "fisso": 4.0, "km": 0.8},
            "3": {"nome": "Burger", "fisso": 3.0, "km": 0.6}
        }

        r = ristoranti[rist_id]
        
        # Calcoli
        sconto = 0.10 if importo > 30 else 0.0
        imp_scontato = importo * (1 - sconto)
        consegna = r['fisso'] + (distanza * r['km'])
        totale = imp_scontato + consegna

        # Prepariamo la risposta come stringa
        risposta = f"{imp_scontato:.2f};{consegna:.2f};{totale:.2f}"
        conn.sendall(risposta.encode('utf-8'))
    except Exception as e:
        print(f"Errore durante la gestione di {addr}: {e}")
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 65432))
    server.listen()
    print("Server pronto e in ascolto...")

    while True:
        conn, addr = server.accept()
        # Creiamo un thread per ogni nuovo client
        thread = threading.Thread(target=gestisci_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()