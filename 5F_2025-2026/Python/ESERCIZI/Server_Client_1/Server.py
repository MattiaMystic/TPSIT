import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Usa il tuo IP reale (es: 192.168.1.100)
    server_socket.bind(('192.168.60.180', 12345))
    server_socket.listen(5)
    print("Server in ascolto sulla porta 12345...")
    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Connessione stabilita con {addr}")

            data = conn.recv(1024).decode()
            print(f"Messaggio ricevuto: {data}")

            response = "Ciao dal server!"
            conn.send(response.encode())

            conn.close()
    except KeyboardInterrupt:
        print("\nServer interrotto")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()