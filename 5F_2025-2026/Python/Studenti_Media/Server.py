import socket

def calcola(nome,voti):
    somma=0
    for v in voti:
        somma=somma+v
        
    media = somma/len(voti)
    
    if media>=6:
        stato="Promosso"
    elif media>=5:
        stato="Rimandato"
    else:
        stato="Bocciato"
        
    minimo=voti[0]
    massimo= voti[0]
    
    for v in voti:
        if v<minimo:
            minimo=v
        if v>massimo:
            massimo=v
    return nome + "," +str(round(media,2)) + "," + stato + "," + str(massimo) + "," + str(minimo)

def start_server():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 12345))
    
    server.listen(1)
    while True:
        conn, addr= server.accept()
        
        dati = conn.recv(1024).decode()
        parti = dati.split(";")
        nome=parti[0]
        
        voti_str= parti[1].split(",")
        
        voti=[]
        for v in voti_str:
            if v != "": 
                voti.append(float(v))
        risultato = calcola(nome,voti)
        
        conn.send(risultato.encode())
        
        conn.close()

if __name__ == "__main__":
    start_server()
    
