import socket
import random

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    numero = random_numero()
    # Converti l'intero in stringa prima di codificare
    client_socket.sendall(str(numero).encode())

    data = client_socket.recv(1024).decode()
    print(f"Inviato: {numero} | Risposta dal server: {data}")

    client_socket.close()

def random_numero():
    # Corretto: randint invece di randomint
    return random.randint(1, 100)

if __name__ == "__main__":
    start_client()