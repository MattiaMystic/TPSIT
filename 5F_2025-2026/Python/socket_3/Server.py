import socket

def start_server():
    # Disponibilità iniziale taxi
    disponibilita_taxi = 10

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(1)

    print("Centrale Taxi in ascolto sulla porta 12345...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connessione stabilita con {addr}")

        
        data = conn.recv(1024).decode()
        if not data:
            conn.close()
            continue

        partenza, arrivo = data.split(",")

        if disponibilita_taxi > 0:
            disponibilita_taxi -= 1
            response = (
                f"Taxi disponibile!\n"
                f"Partenza: {partenza}\n"
                f"Arrivo: {arrivo}\n"
                f"Taxi rimasti: {disponibilita_taxi}"
            )
        else:
            response = "Nessun taxi disponibile al momento."

        conn.send(response.encode())


        conn.close()
        print(f"Connessione chiusa con {addr}")

if __name__ == "__main__":
    start_server()
