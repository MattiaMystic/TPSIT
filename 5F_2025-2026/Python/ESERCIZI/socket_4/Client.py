import socket
import tkinter as tk
from tkinter import messagebox

# Connessione al server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

def invia_richiesta():
    partenza = entry_partenza.get()
    arrivo = entry_arrivo.get()

    if not partenza or not arrivo:
        messagebox.showerror("Errore", "Inserisci entrambe le città")
        return

    try:
        richiesta = f"{partenza},{arrivo}"
        client_socket.sendall(richiesta.encode())

        risposta = client_socket.recv(1024).decode()
        messagebox.showinfo("Risposta Centrale Taxi", risposta)

        entry_partenza.delete(0, tk.END)
        entry_arrivo.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Errore", str(e))
        client_socket.close()
        root.destroy()

# Creazione finestra
root = tk.Tk()
root.title("Prenotazione Taxi")

tk.Label(root, text="Città di partenza").pack(pady=5)
entry_partenza = tk.Entry(root)
entry_partenza.pack(pady=5)

tk.Label(root, text="Città di arrivo").pack(pady=5)
entry_arrivo = tk.Entry(root)
entry_arrivo.pack(pady=5)

tk.Button(root, text="Verifica disponibilità", command=invia_richiesta).pack(pady=10)

root.mainloop()
