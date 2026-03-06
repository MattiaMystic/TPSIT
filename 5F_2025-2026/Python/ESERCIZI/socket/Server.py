import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server in ascolto sulla porta 12345...")
    
    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Connessione da {addr}")

            data = conn.recv(1024).decode()
            if not data: break
            
            # Converti in intero per il confronto numerico
            numero = int(data)
            print(f"Ricevuto: {numero}")

            if numero < 30:
                response = "Troppo basso!"
            else:
                response = "HAI VINTO!"
            
            # Corretto: encode() invece di endcode()
            conn.send(response.encode())
            conn.close()
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
