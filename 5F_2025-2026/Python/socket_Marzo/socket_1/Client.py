import socket

def main():
    print("1. Pizzeria\n2. Sushi\n3. Burger")
    scelta = input("Scegli (1-3): ")
    
    try:
        importo = input("Importo cibo: ")
        distanza = input("Distanza km: ")

        # Validazione base locale
        if float(importo) <= 0 or float(distanza) <= 0:
            print("Errore: inserire valori positivi.")
            return

        # Creiamo la stringa da inviare
        messaggio = f"{scelta};{importo};{distanza}"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 65432))
        s.sendall(messaggio.encode('utf-8'))

        # Riceviamo la risposta
        risposta_raw = s.recv(1024).decode('utf-8')
        dati_finali = risposta_raw.split(';')

        print(f"\nRisultato:")
        print(f"Cibo scontato: {dati_finali[0]}€")
        print(f"Consegna: {dati_finali[1]}€")
        print(f"TOTALE: {dati_finali[2]}€")
        
        s.close()
    except ValueError:
        print("Errore: inserisci numeri validi.")
    except Exception as e:
        print(f"Errore connessione: {e}")

if __name__ == "__main__":
    main()