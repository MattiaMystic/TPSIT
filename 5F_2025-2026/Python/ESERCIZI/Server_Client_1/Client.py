import socket
import tkinter as tk
from tkinter import messagebox

# Impostazioni del server
HOST = "192.168.60.143"   # Indirizzo IP del server (localhost)
PORT = 5000          # Porta su cui il server è in ascolto


def invia_messaggio():
    """
    Questa funzione viene eseguita quando premi il pulsante "Invia al server".
    Legge il testo dall'Entry, apre una connessione socket, invia il messaggio
    e riceve la risposta dal server.
    """

    msg = entry.get()   # Legge il contenuto inserito nella casella di testo

    # Controlla se l'utente ha lasciato il campo vuoto
    if msg.strip() == "":
        messagebox.showwarning("Attenzione", "Inserisci un messaggio")
        return

    try:
        # Crea la socket del client
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            # Si connette al server (IP e porta)
            client.connect((HOST, PORT))

            # Invia il messaggio trasformandolo in bytes
            client.sendall(msg.encode())

            # Riceve la risposta del server (max 1024 byte)
            risposta = client.recv(1024).decode()

        # Mostra la risposta in una finestra popup
        messagebox.showinfo("Risposta del server", risposta)

    except ConnectionRefusedError:
        # Caso in cui il server NON è avviato
        messagebox.showerror("Errore", "Il server non è attivo.")


# ===============================
#       COSTRUZIONE GUI
# ===============================

root = tk.Tk()            # Crea la finestra principale
root.title("Client Python")

# Frame per contenere gli elementi grafici (solo estetica)
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Etichetta
label = tk.Label(frame, text="Inserisci messaggio:")
label.pack()

# Casella di input
entry = tk.Entry(frame, width=40)
entry.pack(pady=10)

# Pulsante che richiama invia_messaggio()
btn = tk.Button(frame, text="Invia al server", command=invia_messaggio)
btn.pack()

# Avvia il loop grafico della finestra
root.mainloop()